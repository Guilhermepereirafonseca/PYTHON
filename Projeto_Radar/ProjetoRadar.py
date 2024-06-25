import numpy as np # numpy vai chamar np

import matplotlib # Biblioteca matemática do python

matplotlib.use('TkAgg') # Utilizando o visual da mesma

import matplotlib.pyplot as plt # Atributo da biblioteca vai chamar plt

from matplotlib.widgets import Button # Importando o botão de widgets (matplotlib)

import serial,sys,glob # Biblioteca para identificar as portas, sistema, mexer com linux (partições)

import serial.tools.list_ports as COMs # serial.tools.list_ports vai se chamar COMs



def port_search(): # Função para procurar as portas

   if sys.platform.startswith('win'): # Windows

       ports = ['COM{0:1.0f}'.format(ii) for ii in range(1,256)]

   elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):

       ports = glob.glob('/dev/tty[A-Za-z]*')

   elif sys.platform.startswith('darwin'): # MAC

       ports = glob.glob('/dev/tty.*')

   else:

       raise EnvironmentError('Máquina Não Compatível com Pyserial') # Definindo o erro e sua saída

   arduinos = [] # Lista das portas

   for port in ports: # loop through to determine if accessible

       if len(port.split('Bluetooth'))>1:

           continue

       try:

           ser = serial.Serial(port)

           ser.close()

           arduinos.append(port) # if we can open it, consider it an arduino

       except (OSError, serial.SerialException):

           pass

   return arduinos

arduino_ports = port_search()

ser = serial.Serial(arduino_ports[0],baudrate=115200) # match baud no Arduino

ser.flush() # clear the port

#

############################################

# Inicie a ferramenta de plotagem interativa e

# plotar 180 graus com dados fictícios para começar

############################################

#

fig = plt.figure(facecolor='k') # Cor da figura

win = fig.canvas.manager.window # janela de figura

screen_res = win.wm_maxsize() # usado para formatação de janela posterior

dpi = 150.0 # Resolução da figura

fig.set_dpi(dpi) # set resolution figure

# atributos do gráfico polar e condições iniciais

ax = fig.add_subplot(111,polar=True,facecolor='#006d70')

ax.set_position([-0.05,-0.05,1.1,1.05])

r_max = 100.0 # pode mudar isso com base na faixa do sensor

ax.set_ylim([0.0,r_max]) # gama de distâncias para mostrar

ax.set_xlim([0.0,np.pi]) # limitado pela amplitude do servo (0-180 graus)

ax.tick_params(axis='both',colors='w')

ax.grid(color='w',alpha=0.5) # cor da grade

ax.set_rticks(np.linspace(0.0,r_max,5)) # show 5 different distances

ax.set_thetagrids(np.linspace(0.0,180.0,10)) # mostrar 10 ângulos

angles = np.arange(0,181,1) # 0 - 180 degrees

theta = angles*(np.pi/180.0) # para radianos

dists = np.ones((len(angles),)) # distâncias fictícias até que dados reais entrem

pols, = ax.plot([],linestyle='',marker='o',markerfacecolor = 'w',

                markeredgecolor='#EFEFEF',markeredgewidth=1.0,

                markersize=10.0,alpha=0.9) # pontos para pontos de radar

line1, = ax.plot([],color='w',

                 linewidth=4.0) # enredo de braço extenso

# ajustes de apresentação de figura

fig.set_size_inches(0.96*(screen_res[0]/dpi),0.96*(screen_res[1]/dpi))

plot_res = fig.get_window_extent().bounds # window extent for centering

win.wm_geometry('+{0:1.0f}+{1:1.0f}'.\

               format((screen_res[0]/2.0)-(plot_res[2]/2.0),

                      (screen_res[1]/2.0)-(plot_res[3]/2.0))) # plotagem de centralização

fig.canvas.toolbar.pack_forget() # remova a barra de ferramentas para uma apresentação limpa

fig.canvas.set_window_title('Arduino Radar')

fig.canvas.draw() # desenhar antes do laço

axbackground = fig.canvas.copy_from_bbox(ax.bbox) # background to keep during loop

############################################

# evento de botão para parar o programa

############################################

def stop_event(event):

   global stop_bool

   stop_bool = 1

prog_stop_ax = fig.add_axes([0.85,0.025,0.125,0.05])

pstop = Button(prog_stop_ax,'Stop Program',color='#FCFCFC',hovercolor='w')

pstop.on_clicked(stop_event)

# botão para fechar a janela

def close_event(event):

   global stop_bool,close_bool

   if stop_bool:

       plt.close('all')

   stop_bool = 1

   close_bool = 1

close_ax = fig.add_axes([0.025,0.025,0.125,0.05])

close_but = Button(close_ax,'Close Plot',color='#FCFCFC',hovercolor='w')

close_but.on_clicked(close_event)

fig.show()

############################################

# loop infinito, atualizando constantemente o

# 180deg radar com entrada de dados do Arduino

############################################

#

start_word,stop_bool,close_bool = False,False,False

while True:

   try:

       if stop_bool: # pára o programa

           fig.canvas.toolbar.pack_configure() # mostrar barra de ferramentas

           if close_bool: # fecha a janela do radar

               plt.close('all')

           break

       ser_bytes = ser.readline() # ler dados seriais do Arduino

       decoded_bytes = ser_bytes.decode('utf-8') # decodificar dados para utf-8 (acentuação)

       data = (decoded_bytes.replace('\r','')).replace('\n','')

       if start_word:

           vals = [float(ii) for ii in data.split(',')]

           if len(vals)<2:

               continue

           angle,dist = vals # separar em ângulo e distância

           if dist>r_max:

               dist = 0.0 # medindo mais do que r_max, é provavelmente impreciso

           dists[int(angle)] = dist

           if angle % 5 ==0: # update every 5 degrees

               pols.set_data(theta,dists)

               fig.canvas.restore_region(axbackground)

               ax.draw_artist(pols)

               line1.set_data(np.repeat((angle*(np.pi/180.0)),2),

                  np.linspace(0.0,r_max,2))

               ax.draw_artist(line1)

               fig.canvas.blit(ax.bbox) # replantar apenas dados

               fig.canvas.flush_events() # flush for next plot

       else:

           if data=='Radar Start': # começar palavra no Arduino

               start_word = True # espere que o Arduino produza a palavra inicial

               print('Radar Starting...')

           else:

               continue



   except KeyboardInterrupt:

       plt.close('all')

       print('Keyboard Interrupt')

       break