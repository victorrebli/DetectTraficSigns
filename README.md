# placas_detectar_1

Como executar o código

Obs:  É necessário  efetuar  os  downloads  da  base  de  dados  GTSRB(conjunto de treinamento e testes)  e  GTSDB(conjunto de treinamento e testes)
GTSRB:  http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset
GTSDB:  http://benchmark.ini.rub.de/?section=gtsdb&subsection=dataset
 Os  arquivos  "insericao_labels.py"  e   "selecionar_dados.py"  foram  os arquivos utilizados  para  a  preparação do conjunto  de treinamento e testes e a inserção  dos labels  nos arquivos  contendo  o caminho  das imagens de treinamento e testes,  então  por  favor  alterar  os  caminhos  absolutos  de onde-se  encontra-se  as  bases.    
1)  O  treinamento  da  rede  neural  precisa ser  realizado, e os pesos  encontra-se  dentro da pasta "meu_modelo/teste" , mas caso fosse necessário  treinar  novamente  a base ,  basta  realizar  o  seguinte  comando :
 1.1)  Os  arquivos  binaryproto  e  a base  de dados  lmdb  devem ser  criados;  executar  os  dois  seguintes  comandos:
       1.2)   GLOG_logtostderr=1  path/to /caffe/build/tools/convert_imageset --resize_height=256  --resize_width=256  --shuffle   path/to/placas5_preto/positivos/    path/to/placas5_preto/exemplos_train_bkp.txt   path/to/placas5_preto/train_lmdb
       1.3)  path/to/caffe/build/tools/compute_image_mean   path/to/placas5_preto/train_lmdb        path/to/placas5_preto/binaryproto
2)  Para  executar  a  rede  neural  no  caffe, que iniciará o treinamento,   é  necessário  colocar  a  pasta  "meu_modelo", dentro  do  diretorio  " path/to/caffe/models".
 3)  Alterar  o  arquivo  train_val.prototxt,   indicando  o  caminho  da   pasta  "placas5_preto/binaryproto",  "placas5_preto/exemplos_train.txt",  "placas5_preto/exemplos_teste.txt"  e  no  arquivo  solver.prototxt ,  indicando  o  caminho para  "path/to/caffe/models/meu_modelo/train_val.prototxt"  e  "path/to/caffe/models/meu_modelo/train"
  4) Executar   o  código   " path/to/caffe/build/tools/caffe train  --solver  path/caffe/models/meu_modelo/solver.prototxt"  
5)  Uma  vez  terminado  o  treinamento,  execute  o  procedimento  para  utilizar   as  imagens  de  testes  para   iniciar  a detecção  de  placas  por  meio do  arquivo  "detecta_placa.py" -  Por  favor  altere  o  caminho  absoluto  base  "teste_jpg"
