# MADT_HL_Fabric

## Подготовка к запуску:
1. Установите docker, docker-compose, go, python3, pip3

Далее приведены команды по установке для Ubunty 20.04

```
cd ~
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo apt install golang-go
sudo apt install python3
sudo apt install python3-pip
```
2. Далее необходимо склонировать и собрать образы и бинарники для Hyperledger fabric

```
cd ~
curl -sSL https://bit.ly/2ysbOFE | bash -s
```
3. Далее склонируем и установим все зависимости для MADT

```
cd ~
git clone --recursive https://github.com/dltcspbu/madt/
mkdir ~/madt/labs && export MADT_LABS_DIR=$HOME/madt/labs
mkdir ~/madt/sockets && export MADT_LABS_SOCKETS_DIR=$HOME/madt/sockets

cd madt
sudo pip3 install -r ./requirements.txt
sudo make && sudo make install
```
4. Клонируем этот репозиторий
```
cd ~
cd fabric-samples
git clone https://github.com/NightBlade97/Madt_HL_Fabric.git

```

## Тестирование в MADT
1. Запустим  MADT
```
cd ~
cd madt
sudo -HE env PYTHONPATH=$HOME/madt:$PYTHONPATH SSH_PWD=demo python3 madt_ui/main.py 80
```

2. Запустим lab
```
#open new terminal window
cd ~
cd fabric-samples/Madt_HL_Fabric
python3 ./lab.py
```
3. Откройте 127.0.0.1:80
4. Войдите как `demo:demo`
5. Выберете созданную сеть и нажмите `restart`, дождитесь завершения работы.
6. 


## Тестирование вне MADT
1. Перейдем в рабочую директорию
```
cd ~
cd fabric-samples/Madt_HL_Fabric

```
2. Запустим сеть и создадим Fabric channel для транзакций между Org1 and Org2. 
```
./network.sh up createChannel
```
3. Установим fabcar chaincode для Org1 и Org2, а затем развернем chaincode на созданном на предыдущем шаге канале
```
./network.sh deployCC
```
Так же предыдущая команада добавляет в реестр базовый список машин 
4. Далее проведем базовую операцию, чтобы проверить, что все работает
```
bash scripts/basicOrder.sh
```
В данном скрипте изменяется владелец машины номер 9.
Если в результаты выполнения скрипта получается вот такой вывод, то все прошло успешно:
```
chaincodeInvokeOrQuery -> INFO 001 Chaincode invoke successful. result: status:200
```