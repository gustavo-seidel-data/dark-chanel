from moviepy import VideoFileClip, TextClip, ColorClip, CompositeVideoClip
import os

video_folder = "/home/gustavoseidel51/youtube/videos/"
clip_path = "/home/gustavoseidel51/youtube/clipedvideo/"
list_title = ["Esse foi ver estrelas", "Glitch TV Station", "Treta revelada","Doc Secreto *****", "Exorcisando os Bot", "Será que era Ghost"]

def cut_video(start_time,end_time,path):
    # Carrega o vídeo
    video = VideoFileClip(path)
    # Define o intervalo que você quer cortar (exemplo: do segundo 10 ao 20)
    start_time = 2
    end_time = 3
    # Faz o corte
    video_cortado = video.subclipped(start_time, end_time)
    # Salva o vídeo cortado
    video_cortado.write_videofile("/home/gustavoseidel51/youtube/clipedvideo/cut_video.mp4", codec="libx264")

def tarj_video(input,output):
    for data_file in input:
        # Carrega o vídeo original
        file_name = data_file[0]
        title = data_file[1]
        video = VideoFileClip(file_name)

        # Define a duração da tarja igual à do vídeo cortado (ou do vídeo todo)
        duracao = video.duration

        # Cria a tarja vermelha (exemplo: altura 50 pixels, largura igual ao vídeo)
        tarja = ColorClip(size=(video.w, 50), color=(255, 0, 0)).with_duration(duracao)

        # Cria o texto (ajuste fonte, tamanho e cor conforme desejar)
        texto = TextClip(
            text = title, 
            font_size=30, 
            stroke_color='black',
            stroke_width=2,
            color='white', 
            method='label'
            )

        posicao_y = video.h // 2 - 380  # 100 pixels acima do centro
        tarja = tarja.with_position(('center', posicao_y))
        texto = texto.with_position(('center', posicao_y)).with_duration(duracao)

        # Cria o vídeo final combinando o vídeo original + tarja + texto
        video_final = CompositeVideoClip([video, tarja, texto])

        # Salva o resultado
        video_final.write_videofile(f"{output}/processed_{file_name.split('/')[-1]}", codec="libx264")

def read_files(input_folder):
    list_file_name = []
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
            list_file_name.append(os.path.join(input_folder, file_name))
    return list_file_name

def add_frase(list_file_name,list_title):
    compose_list_title = []
    for file_name,title in zip(list_file_name,list_title):
        compose_list_title.append([file_name,title])
    return compose_list_title


files_path_name = read_files(video_folder)
compose_list_title = add_frase(files_path_name,list_title)
tarj_video(compose_list_title,clip_path)




