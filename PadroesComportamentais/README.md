# Command, Comando, Ação, Action, Transação, Transaction

1. Créditos: https://refactoring.guru/pt-br/design-patterns/command

## Propósito

O Command é um padrão de projeto comportamental que transforma um pedido em um objeto independente que contém toda a informação sobre o pedido. Essa transformação permite que você parameterize métodos com diferentes pedidos, atrase ou coloque a execução do pedido em uma fila, e suporte operações que não podem ser feitas.

## Problema

Imagine que você está trabalhando em uma nova aplicação de editor de texto. Sua tarefa atual é criar uma barra de tarefas com vários botões para várias operações do editor. Você criou uma classe Botão muito bacana que pode ser usada para botões na barra de tarefas, bem como para botões genéricos de diversas caixas de diálogo.

Embora todos esses botões pareçam similares, eles todos devem fazer coisas diferentes. Aonde você deveria colocar o código para os vários handlers de cliques desses botões? A solução mais simples é criar um monte de subclasses para cada local que o botão for usado. Essas subclasses conteriam o código que teria que ser executado em um clique de botão.

Não demora muito e você percebe que essa abordagem é falha. Primeiro você tem um enorme número de subclasses, e isso seria okay se você não arriscasse quebrar o código dentro dessas subclasses cada vez que você modificar a classe base Botão. Colocando em miúdos: seu código GUI se torna absurdamente dependente de um código volátil da lógica do negócio.

E aqui está a parte mais feia. Algumas operações, tais como copiar/colar texto, precisariam ser invocadas de diversos lugares. Por exemplo, um usuário poderia criar um pequeno botão “Copiar” na barra de ferramentas, ou copiar alguma coisa através do menu de contexto, ou apenas apertando Crtl+C no teclado.

Inicialmente, quando sua aplicação só tinha a barra de ferramentas, tudo bem colocar a implementação de várias operações dentro das subclasses do botão. Em outras palavras, ter o código de cópia de texto dentro da subclasse BotãoCópia parecia certo. Mas então, quando você implementou menus de contexto, atalhos, e outras coisas, você teve que ou duplicar o código da operação em muitas classes ou fazer menus dependentes de botões, o que é uma opção ainda pior.

## Solução

Um bom projeto de software quase sempre se baseia no princípio da separação de interesses, o que geralmente resulta em dividir a aplicação em camadas. O exemplo mais comum: uma camada para a interface gráfica do usuário e outra camada para a lógica do negócio. A camada GUI é responsável por renderizar uma bonita imagem na tela, capturando quaisquer dados e mostrando resultados do que o usuário e a aplicação estão fazendo. Contudo, quando se trata de fazer algo importante, como calcular a trajetória da lua ou compor um relatório anual, a camada GUI delega o trabalho para a camada inferior da lógica do negócio.

Dentro do código pode parecer assim: um objeto GUI chama um método da lógica do negócio, passando alguns argumentos. Este processo é geralmente descrito como um objeto mandando um pedido para outro.

O padrão Command sugere que os objetos GUI não enviem esses pedidos diretamente. Ao invés disso, você deve extrair todos os detalhes do pedido, tais como o objeto a ser chamado, o nome do método, e a lista de argumentos em uma classe comando separada que tem apenas um método que aciona esse pedido.

Objetos comando servem como links entre vários objetos GUI e de lógica de negócio. De agora em diante, o objeto GUI não precisa saber qual objeto de lógica do negócio irá receber o pedido e como ele vai ser processado. O objeto GUI deve acionar o comando, que irá lidar com todos os detalhes.

O próximo passo é fazer seus comandos implementarem a mesma interface. Geralmente é apenas um método de execução que não pega parâmetros. Essa interface permite que você use vários comandos com o mesmo remetente do pedido, sem acoplá-lo com as classes concretas dos comandos. Como um bônus, agora você pode trocar os objetos comando ligados ao remetente, efetivamente mudando o comportamento do remetente no momento da execução.

Você pode ter notado uma peça faltante nesse quebra cabeças, que são os parâmetros do pedido. Um objeto GUI pode ter fornecido ao objeto da camada de negócio com alguns parâmetros, como deveremos passar os detalhes do pedido para o destinatário? Parece que o comando deve ser ou pré configurado com esses dados, ou ser capaz de obtê-los por conta própria.

Vamos voltar ao nosso editor de texto. Após aplicarmos o padrão Command, nós não mais precisamos de todas aquelas subclasses de botões para implementar vários comportamentos de cliques. É suficiente colocar apenas um campo na classe Botão base que armazena a referência para um objeto comando e faz o botão executar aquele comando com um clique.

Você vai implementar um monte de classes comando para cada possível operação e ligá-los aos seus botões em particular, dependendo do comportamento desejado para os botões.

Outros elementos GUI, tais como menus, atalhos, ou caixas de diálogo inteiras, podem ser implementados da mesma maneira. Eles serão ligados a um comando que será executado quando um usuário interage com um elemento GUI. Como você provavelmente adivinhou, os elementos relacionados a mesma operação serão ligados aos mesmos comandos, prevenindo a duplicação de código.

Como resultado, os comandos se tornam uma camada intermédia conveniente que reduz o acoplamento entre as camadas GUI e de lógica do negócio. E isso é apenas uma fração dos benefícios que o padrão Command pode oferecer.