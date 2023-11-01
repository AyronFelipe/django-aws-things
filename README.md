# Django AWS Things

Primeiramente, faça uma cópia do .env.example, renomeando para .env e coloque suas credencias aws nas opções:

```bash
AWS_DEFAULT_REGION=
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```

Para rodar o projeto localmente você precisa ter o docker instalado na sua máquina, para iniciar o projeto django rode o comando abaixo:

```bash
docker compose up --build app
```

Esse comando vai levantar todo o ambiente necessário para poder começar a desenvolver.

## AWS

Aqui você vai ter que ter o aws-cli instalado na sua máquina e configurado se não tem, pode seguir por [aqui](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

Após isso, terá que configurar o sam-cli, pode fazer isso seguindo [essas instruções](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html).

Com o sam-cli configurado entre na pasta aws e rode o comando:

```bash
sam build; sam deploy
```

Quando essa etapa finalizar, pegue o nome da sua lambda criada e coloque como valor da variável de ambiente `LAMBDA_FUNCTION_CALCULATE_DATE_OF_BIRTH_FUNCTION`, rode o comando `docker compose up app` novamente e está pronto para seguir.

## Como testar?

Só rodar o comando:

```bash
docker compose up integration-tests
```

## Documentação

A documentação dos endpoints está disponível nas urls
`iapi/schema/`
`iapi/schema/swagger-ui/`
`iapi/schema/redoc/`

## A solução

Assim que você cria um usuário através do endpoint de criação, uma mensagem é enviada pelo SQS para a nossa lambda lá o ano de nascimento do usuário é calculado e devolvido para a nossa aplicação, em seguida uma mensagem de sucesso é enviada para o SNS.
