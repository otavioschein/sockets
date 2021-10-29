# sockets

Código baseado no [video](https://www.youtube.com/watch?v=3QiPPX-KeSc)

Trabalho de Otávio Schein e Lucca Schein

Realizado em python um chat entre múltiplos usuários, os quais conectam em um server local.


- deve-se rodar o server, o qual rodará em uma porta local;
- rodar um ou mais clients;
  -  Caso rode mais de um, deve inserir o username do primeiro client por primeiro, em seguida o segundo e assim por diante.
- após colocar o username do client, deve-se dar alguns enters para poder de fato funcionar. (Não sei o pq kkk)

Os usuários podem conversar entre si normalmente, respeitando um array de palavras consideradas ofensivas `fuck, shit, cock, pussy`. Caso o ussuário digite uma delas receberá um timeout de 10 segundos, não podendo enviar mais mensagens nesse período, mas poderá receber normalmente.

O usuário ainda pode digitar alguns comandos:
 - /list
    - lista os usuários conectados no servidor;
 - /key
    - lista os comandos que o usuários pode digitar;
 - /exit
    - o client sai do servidor.
