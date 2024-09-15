# django-para-profissionais
Projeto com código fonte do [curso Django para Profissionais](https://l.dev.pro.br/django-para-profissionais.) da DevPro.

[Playlist no YouTube](https://l.dev.pro.br/playlist-django-para-profissionais)

## Instalação

Para instalar o projeto localmente, instale o poetry e use o comando, com dependências desenvolvimento: 

```bash
poetry install --with dev
```

Ative o ambiente virtual:

```bash
poetry shell
```

Definir variáveis de ambiente em um .env de acordo com o [.env-sample](.env-sample)

Rode o servidor local:

```bash
task run
```

Para rodar testes automáticos com pytest:

```bash
task test
```

Para rodar testes automáticos com pytest e gerar relatório de cobertura:

```bash
pytest devpro/ --cov=devpro --cov-report html
```


Utilize também o formato de código configurado com ruff. Você pode consultar todos os gatilhos disponíveis no pyproject.toml:

```
task lint
```

