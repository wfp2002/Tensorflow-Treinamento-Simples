# Tensorflow-Treinamento-Simples
Scripts para treinamentos simples usando tensorflow

Baseado em: https://codelabs.developers.google.com/codelabs/tensorflow-for-poets

Primeiro passo fazer o clone do repositorio:

git clone https://github.com/wfp2002/Tensorflow-Treinamento-Simples.git

Entra na pasta:

cd Tensorflow-Treinamento-Simples


Executar o arquivo de download de imagens, dentro alterar qtde de imagens para baixar e escolher o tema, as imagens serao salvas na pasta downloads:

python3 google-download.py


Apos ter baixados todas as imagens necessarias, criar os diretorios abaixo em "cd Tensorflow-Treinamento-Simples":

mkdir tf_files

cd tf_files

mkdir objetos


E colar todas as pastas de imagens que estao na pasta "download" para essa nova pasta "objetos":

Apos colado voltar para pasta "cd Tensorflow-Treinamento-Simples" e colar no terminal as segintes variaveis de ambiente:


IMAGE_SIZE=224

ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

*** Essas variaveis definem que iremos usar a mobilenet_0.50_224 , outros modelos poderao ser acessados no link: 
https://ai.googleblog.com/2017/06/mobilenets-open-source-models-for.html

Feito isso execute o arquivo

python3 -m retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/objetos


Finalizado o processo, copie algumas imagens baixadas dos objetos para a pasta tf_files/objetos e rode o comando abaixo para identificar a imagem:


python3 -m label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=tf_files/objetos/teste.jpg

Devera sair o Score do objeto detectado.

As pastas tf_files/bottlenecks e tf_files/models/ podem ser deletadas apos o treinamento
