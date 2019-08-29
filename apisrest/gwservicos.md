# Documentação das requisições

**Códigos de Erro:**

0: Mensagem de Sucesso

1: Mensagem de Alerta

2: Mensagem de Erro ou Falha na Execução

999: Chave inválida

### Obtenção do token de acesso

Primeira chamada realizada.

Identifica a empresa e obtém o token que deve ser enviado nas demais requisições.

Retorna o token.

_**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
       "gerarChave": {
               "aplicacao": "6E8E69A8-15ED-44A9-B378-570A8298F776",
               "chave": "beb6b72231daafe7d913baa818a63f0c"
       }
}
"
```

_**Resposta de sucesso:**_

```json
{
	"gerarChave": {
		"chave": "2BBC5CC7-74A4-8480-80E8-22F8AA127AA8",
		"status": 0,
		"mensagem": "Chave Gerada Com Sucesso"
	}
}
```

_**Resposta de erro:**_

```json
{
	"gerarChave": {
		"status": 1,
		"mensagem": "Informe a aplicação para gerar o token"
	}
}

{
	"gerarChave": {
		"status": 1,
		"mensagem": "Informe a senha da aplicação para gerar o token"
	}
}

{
	"gerarChave": {
		"status": 2,
		"mensagem": "Identificação da aplicação inválida ou inativa!"
	}
}

```
### Autenticação

Autenticação do vendedor no aplicativo. Retorna os dados do vendedor

_**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="{
	"autenticacao": {
		"senha_funcionario": "1515",
		"chave": "D5FD19B2-B549-4DD0-8F5F-251E5DA3899E"
	}}"
```

_**Resposta de sucesso:**_

```json
{
	"autenticacao": {
		"status": 0,
		"mensagem": "",
		"codigo_funcionario": 160,
		"nome_funcionario": "SUPORTE",
		"codigo_empresa": 1,
		"nome_empresa": "PAPELARIA ABC",
		"cod_usuario": 1,
		"nome_usuario": "master",
		"config_balanca": "S;2;13;2;4;8;5;1;2",
		"acumula_item": "N",
		"cod_prod_diversos": 0,
		"possui_servico": "N",
		"tem_cashback": "S",
		"observacao_padrao": "VALIDADE DA PROPOSTA: 07 DIAS",
		"nome_orcamento": "ORÇAMENTO",
		"config_possui_lote": "S",
		"critica_por_func": "N",
		"utiliza_balanca": "S",
		"utiliza_mix": "N",
		"config_id_pag_nfe": 0
	}
}
```

_**Resposta de erro:**_

```json
{
	"autenticacao": {
		"status": 2,
		"mensagem": "Não foi possível encontrar um funcionário com esta senha"
	}
}

{
	"autenticacao": {
		"status": 1,
		"mensagem": "A senha informada está associada à mais de um funcionário, não é possível continuar"
	}
}

{
	"autenticacao": {
		"status": 2,
		"mensagem": "Houve uma falha nessa execução, verifique o log dos serviços"
	}
}
```

### Consultar Pedidos

Esta consulta irá retornar os 30 primeiros pedidos que encontrar no banco de dados, visando não pesar o tráfego de informações e ter mais performance. O usuário deverá utilizar dos filtros para encontrar o pedido desejado.

Na consulta de pedidos os seguintes filtros serão aceitos e deverão estar disponíveis no APP:

- Código da Venda

- Vendedor (Código do Vendedor) (Neste caso será uma lista de vendedores numa COMBO, então para alimentá-la deverá ser chamado o serviço de "listar_vendedores")

- Nome do Cliente

- CPF ou CNPJ

- Periodo (Data Inicial e Final) (Estas datas deverão ser enviadas no formato YYYY-MM-DD)

- Empresa (Código da Empresa) (Neste caso será uma lista de empresas numa COMBO, então para alimentá-la deverá ser chamado o serviço de "listar_empresas")

- Código do usuário: Este campo será alimentado com o código de usuário que foi recuperado no serviço de autenticação

  ​

  **observação:** Os campos inteiros como o Código da Venda, Empresa e Vendedor, quando não informados devem ser preenchido com valor zero com aspas

  ​

  _**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="
Exemplo de chamadas com filtros:
{
	"consultar_pedidos": {
		"codigo_venda": "0",
		"vendedor": "0",
		"nome_cliente": "",
		"cpf_cnpj": "",
		"data_inicial": "",
		"data_fnal": "",
		"empresa": "0",
		"cod_usuario": "209",
		"situacao_pedido": "1",
		"chave": "ECD7903D-10DA-70F4-651C-BAB944FBEFA9"
	}
}

{
	"consultar_pedidos": {
		"codigo_venda": "168607",
		"vendedor": "0",
		"nome_cliente": "",
		"cpf_cnpj": "",
		"data_inicial": "",
		"data_fnal": "",
		"empresa": "0",
		"cod_usuario": "209",
		"situacao_pedido": "0",
		"chave": "ECD7903D-10DA-70F4-651C-BAB944FBEFA9"
	}
}

{
	"consultar_pedidos": {
		"codigo_venda": "168607",
		"vendedor": "0",
		"nome_cliente": "ESTETI",
		"cpf_cnpj": "",
		"data_inicial": "",
		"data_fnal": "",
		"empresa": "0",
		"cod_usuario": "209",
		"situacao_pedido": "0",
		"chave": "ECD7903D-10DA-70F4-651C-BAB944FBEFA9"
	}
}

{
	"consultar_pedidos": {
		"codigo_venda": "",
		"vendedor": "0",
		"nome_cliente": "",
		"cpf_cnpj": "000130",
		"data_inicial": "",
		"data_fnal": "",
		"empresa": "0",
		"cod_usuario": "209",
		"situacao_pedido": "0",
		"chave": "ECD7903D-10DA-70F4-651C-BAB944FBEFA9"
	}
}

{
	"consultar_pedidos": {
		"codigo_venda": "",
		"vendedor": "0",
		"nome_cliente": "",
		"cpf_cnpj": "",
		"data_inicial": "2018-03-01",
		"data_fnal": "2018-03-15",
		"empresa": "0",
		"cod_usuario": "209",
		"situacao_pedido": "0",
		"chave": "ECD7903D-10DA-70F4-651C-BAB944FBEFA9"
	}
}
```

_**Resposta de sucesso:**_

```json
EXEMPLO DE RETORNO DE UMA VENDA COM VÁROS ITENS E VÁRIAS FORMAS DE PAGAMENTO
{
	"consultar_pedidos": {
		"status": 0,
		"mensagem": "",
		"pedidos": [{
			"codigo_venda": 168525,
			"situacao_venda": "Finalizada",
			"cor_situacao": "#8cc739",
			"data_hora": "08/03/2018 15:16:40",
			"cliente_cadastrado": "CONSUMIDOR FINAL",
			"cliente_venda": "CONSUMIDOR FINAL",
			"cpf_cnpj": "70874719100",
			"vendedor_venda": "JOSÉ APARECIDO GONÇALVES DA SILVA",
			"empresa": "PAPELARIA ABC",
			"numero_nfce": "124803",
			"numero_nfe": "",
			"perfil_cliente": "LOJA ABC",
			"nome_frete": "",
			"natureza_cfop": "5102 - Vendas Merc. Dent. Est.",
			"cod_troca": "",
			"observacao": "VALIDADE DA PROPOSTA: 07 DIAS",
			"quantidade_itens": "5",
			"subtotal": "254,02",
			"total_desconto": "0,00",
			"total_acrescimos": "0,00",
			"taxa_entrega": "0,00",
			"total_venda": "254,02",
			"itens_venda": [{
				"codigo_item_venda": 1156469,
				"codigo_produto": 4063245,
				"codigo_personalizado": "",
				"codigo_barras": "7899097006834",
				"codigo_apresentacao": "4063245",
				"nome_produto": "ELASTICO P/CADERNO LB",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "19,90",
				"valor_desconto": "0,00",
				"total_produto": "19,90",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "ZEZINHO",
				"observacao": ""
			}, {
				"codigo_item_venda": 1156468,
				"codigo_produto": 970085,
				"codigo_personalizado": "",
				"codigo_barras": "7897478405962",
				"codigo_apresentacao": "970085",
				"nome_produto": "CAIXA ORGANIZADORA POLYCART MEDIA 7011 PT",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "24,90",
				"valor_desconto": "0,00",
				"total_produto": "24,90",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "ZEZINHO",
				"observacao": ""
			}, {
				"codigo_item_venda": 1156466,
				"codigo_produto": 4024664,
				"codigo_personalizado": "",
				"codigo_barras": "7896009764202",
				"codigo_apresentacao": "4024664",
				"nome_produto": "PILHA RAYOVAC ALCALINA PALITO AAA 1,5V 6X1 1649",
				"sigla_unidade": "BL",
				"quantidade_itens": "1",
				"valor_venda": "18,90",
				"valor_desconto": "0,00",
				"total_produto": "18,90",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "ZEZINHO",
				"observacao": ""
			}, {
				"codigo_item_venda": 1156464,
				"codigo_produto": 88536,
				"codigo_personalizado": "",
				"codigo_barras": "012502619673",
				"codigo_apresentacao": "88536",
				"nome_produto": "ROTULADOR ELETRONICO BROTHER PT-70",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "189,90",
				"valor_desconto": "0,00",
				"total_produto": "189,90",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "ZEZINHO",
				"observacao": ""
			}, {
				"codigo_item_venda": 1156463,
				"codigo_produto": 4099828,
				"codigo_personalizado": "",
				"codigo_barras": "7909107664029",
				"codigo_apresentacao": "4099828",
				"nome_produto": "SACO PRES CROMUS 35X54 VALENTIM 99002613",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "0,42",
				"valor_desconto": "0,00",
				"total_produto": ",42",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "ZEZINHO",
				"observacao": ""
			}],
			"formas_pagamento": [{
				"cod_pagamento": 162715,
				"forma_pagamento": "Cartão Visa - Crédito",
				"cod_autorizador": "",
				"vencimento": "07/04/2018",
				"numero_documento": "1/2",
				"valor_parcela": "127,01"
			}, {
				"cod_pagamento": 162716,
				"forma_pagamento": "Cartão Visa - Crédito",
				"cod_autorizador": "",
				"vencimento": "07/05/2018",
				"numero_documento": "2/2",
				"valor_parcela": "127,01"
			}]
		}]
	}
}

RETORNO COM VÁRIAS VENDAS
{
	"consultar_pedidos": {
		"status": 0,
		"mensagem": "",
		"pedidos": [{
			"codigo_venda": 168637,
			"situacao_venda": "Finalizada",
			"cor_situacao": "#8cc739",
			"data_hora": "08/03/2018 18:00:45",
			"cliente_cadastrado": "CONSUMIDOR FINAL",
			"cliente_venda": "CONSUMIDOR FINAL",
			"cpf_cnpj": "66595045168",
			"vendedor_venda": "OSELINA FERREIRA DE BRITO",
			"empresa": "PAPELARIA ABC",
			"numero_nfce": "124873",
			"numero_nfe": "",
			"perfil_cliente": "LOJA ABC",
			"nome_frete": "",
			"natureza_cfop": "5102 - Vendas Merc. Dent. Est.",
			"cod_troca": "",
			"observacao": "VALIDADE DA PROPOSTA: 07 DIAS",
			"quantidade_itens": "1",
			"subtotal": "12,90",
			"total_desconto": "0,00",
			"total_acrescimos": "0,00",
			"taxa_entrega": "0,00",
			"total_venda": "12,90",
			"itens_venda": [{
				"codigo_item_venda": 1157085,
				"codigo_produto": 4099256,
				"codigo_personalizado": "",
				"codigo_barras": "",
				"codigo_apresentacao": "4099256",
				"nome_produto": "FITA CREPE MARRON 50X50 SK770 ALLTAPE",
				"sigla_unidade": "RL",
				"quantidade_itens": "1",
				"valor_venda": "12,90",
				"valor_desconto": "0,00",
				"total_produto": "12,90",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "ZELIA",
				"observacao": ""
			}],
			"formas_pagamento": [{
				"cod_pagamento": 162805,
				"forma_pagamento": "Cartão Visa - Crédito",
				"cod_autorizador": "001863",
				"vencimento": "07/04/2018",
				"numero_documento": "1/1",
				"valor_parcela": "12,90"
			}]
		}, {
			"codigo_venda": 168634,
			"situacao_venda": "Finalizada",
			"cor_situacao": "#8cc739",
			"data_hora": "08/03/2018 17:53:51",
			"cliente_cadastrado": "CONSUMIDOR FINAL",
			"cliente_venda": "CONSUMIDOR FINAL",
			"cpf_cnpj": "02819697607",
			"vendedor_venda": "CARMEM LÚCIA DOS SANTOS OLIVEIRA",
			"empresa": "PAPELARIA ABC",
			"numero_nfce": "124871",
			"numero_nfe": "",
			"perfil_cliente": "LOJA ABC",
			"nome_frete": "",
			"natureza_cfop": "5102 - Vendas Merc. Dent. Est.",
			"cod_troca": "",
			"observacao": "VALIDADE DA PROPOSTA: 07 DIAS",
			"quantidade_itens": "5",
			"subtotal": "55,37",
			"total_desconto": "0,00",
			"total_acrescimos": "0,00",
			"taxa_entrega": "0,00",
			"total_venda": "55,37",
			"itens_venda": [{
				"codigo_item_venda": 1157073,
				"codigo_produto": 4092405,
				"codigo_personalizado": "",
				"codigo_barras": "7898359171211",
				"codigo_apresentacao": "4092405",
				"nome_produto": "JOGO IMOBILIARIO PMBI CAIXA",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "28,99",
				"valor_desconto": "0,00",
				"total_produto": "28,99",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "CARMEM",
				"observacao": ""
			}, {
				"codigo_item_venda": 1157072,
				"codigo_produto": 557757,
				"codigo_personalizado": "",
				"codigo_barras": "",
				"codigo_apresentacao": "557757",
				"nome_produto": "SACO PRESENTE GRANDE SORTIDO",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "3,50",
				"valor_desconto": "0,00",
				"total_produto": "3,50",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "CARMEM",
				"observacao": ""
			}, {
				"codigo_item_venda": 1157070,
				"codigo_produto": 4098923,
				"codigo_personalizado": "",
				"codigo_barras": "7897476652146",
				"codigo_apresentacao": "4098923",
				"nome_produto": "FITA CORRETIVA MINI LAYER 652139 TRIS",
				"sigla_unidade": "UN",
				"quantidade_itens": "2",
				"valor_venda": "5,99",
				"valor_desconto": "0,00",
				"total_produto": "11,98",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "CARMEM",
				"observacao": ""
			}, {
				"codigo_item_venda": 1157069,
				"codigo_produto": 293300,
				"codigo_personalizado": "",
				"codigo_barras": "7899097000214",
				"codigo_apresentacao": "293300",
				"nome_produto": "ESTOJO LB PALITO TELA",
				"sigla_unidade": "UN",
				"quantidade_itens": "1",
				"valor_venda": "10,90",
				"valor_desconto": "0,00",
				"total_produto": "10,90",
				"data_hora_cadastro": "01/01/0001 00:00",
				"hora_cadastro": "00:00",
				"vendedor_item": "CARMEM",
				"observacao": ""
			}],
			"formas_pagamento": [{
				"cod_pagamento": 162803,
				"forma_pagamento": "Cartão Master - Crédito",
				"cod_autorizador": "",
				"vencimento": "07/04/2018",
				"numero_documento": "1/1",
				"valor_parcela": "55,37"
			}]
		}]
	}
}
                    
ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS                    
{
	"consultar_pedidos": {
		"status": 0,
		"mensagem": "",
		"pedidos": []
	}
}
```

_**Resposta de erro:**_

```json
{
	"consultar_pedidos": {
		"status": 999,
		"mensagem": "Chave inválida ou inativa!"
	}
}

{
	"consultar_pedidos": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
{
	"consultar_pedidos": {
		"status": 1,
		"mensagem": "Informe o código do usuário"
	}
}
```

### 

### Listar Vendedores

Lista todos os vendedores das empresas que o usuário logado tem acesso, para escolher numa combo de filtro o vendedor desejado

_**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_vendedores": {
		"cod_usuario": "209",
		"chave": "05FE6359-DB53-1D2B-0840-6C84B3CA25AC"
	}
}"
```

_**Resposta de sucesso:**_

```json
{
	"listar_vendedores": {
      	"status": 0,
		"mensagem": "",
		"vendedores": [{
			"codigo_vendedor": 44,
			"codigo_personalizado": "",
			"apelido_vendedor": "ALEXA",
			"nome_vendedor": "ALEXA DE OLIVEIRA BARBOSA"
		}, {
			"codigo_vendedor": 76,
			"codigo_personalizado": "",
			"apelido_vendedor": "ALINE",
			"nome_vendedor": "ALINE GOMES DOS SANTOS"
		}, {
			"codigo_vendedor": 542,
			"codigo_personalizado": "",
			"apelido_vendedor": "ALVES",
			"nome_vendedor": "DOMINGOS ALVES DE SOUZA"
		}, {
			"codigo_vendedor": 138,
			"codigo_personalizado": "",
			"apelido_vendedor": "AMARILDO",
			"nome_vendedor": "AMARILDO"
		}, {
			"codigo_vendedor": 697,
			"codigo_personalizado": "",
			"apelido_vendedor": "ANA MARIA",
			"nome_vendedor": "ANA MARIA PEREIRA DOS SANTOS"
		}, {
			"codigo_vendedor": 686,
			"codigo_personalizado": "",
			"apelido_vendedor": "ANGELICA",
			"nome_vendedor": "ANGELICA ANDRADE LUIZ"
		}, {
			"codigo_vendedor": 54,
			"codigo_personalizado": "",
			"apelido_vendedor": "ANIELLE",
			"nome_vendedor": "ANIELLE BARBOSA DASILVA"
		}, {
			"codigo_vendedor": 627,
			"codigo_personalizado": "",
			"apelido_vendedor": "ANTONIO VIEIRA",
			"nome_vendedor": "ANTONIO VIEIRA DA SILVA"
		}, {
			"codigo_vendedor": 545,
			"codigo_personalizado": "",
			"apelido_vendedor": "ARISTEA",
			"nome_vendedor": "ARISTEA CHEILA REIS  DE OLIVEIRA"
		}, {
			"codigo_vendedor": 84,
			"codigo_personalizado": "",
			"apelido_vendedor": "ARLINDO",
			"nome_vendedor": "ARLINDO JOSE SOARES"
		}, {
			"codigo_vendedor": 57,
			"codigo_personalizado": "",
			"apelido_vendedor": "AURIDEIA",
			"nome_vendedor": "AURIDEIA MEDEIROS DA SILVA"
		}, {
			"codigo_vendedor": 631,
			"codigo_personalizado": "",
			"apelido_vendedor": "AURIMAR",
			"nome_vendedor": "MARIA AURIMAR CUNHA DE FREITAS"
		}, {
			"codigo_vendedor": 668,
			"codigo_personalizado": "",
			"apelido_vendedor": "BETÂNIA BARBOSA SILV",
			"nome_vendedor": "BETÂNIA BARBOSA SILVA"
		}, {
			"codigo_vendedor": 87,
			"codigo_personalizado": "",
			"apelido_vendedor": "BRUNA MAGNA",
			"nome_vendedor": "Bruna Magna"
		}, {
			"codigo_vendedor": 81,
			"codigo_personalizado": "",
			"apelido_vendedor": "BRUNA THOMAZ",
			"nome_vendedor": "BRUNA DE SOUZA THOMAZ"
		}, {
			"codigo_vendedor": 144,
			"codigo_personalizado": "",
			"apelido_vendedor": "CAMILA",
			"nome_vendedor": "CAMILA ALVES PINHEIRO"
		}, {
			"codigo_vendedor": 692,
			"codigo_personalizado": "",
			"apelido_vendedor": "CARLINHOS",
			"nome_vendedor": "ANTONIO CARLOS ALVES DE FRANÇA"
		}, {
			"codigo_vendedor": 639,
			"codigo_personalizado": "",
			"apelido_vendedor": "CARMEM",
			"nome_vendedor": "CARMEM LÚCIA DOS SANTOS OLIVEIRA"
		}, {
			"codigo_vendedor": 646,
			"codigo_personalizado": "12629",
			"apelido_vendedor": "CAROL",
			"nome_vendedor": "ANA CAROLINA FELIX"
		}, {
			"codigo_vendedor": 59,
			"codigo_personalizado": "",
			"apelido_vendedor": "CAROLINE",
			"nome_vendedor": "CAROLINE ALVES DE SOUSA"
		}, {
			"codigo_vendedor": 99,
			"codigo_personalizado": "",
			"apelido_vendedor": "CAROLINE",
			"nome_vendedor": "CAROLINE BUENO FERREIRA"
		}, {
			"codigo_vendedor": 90,
			"codigo_personalizado": "",
			"apelido_vendedor": "CAROLINE",
			"nome_vendedor": "CAROLINE"
		}, {
			"codigo_vendedor": 155,
			"codigo_personalizado": "",
			"apelido_vendedor": "CELESTINO",
			"nome_vendedor": "CELESTINO FERREIRA FILHO"
		}, {
			"codigo_vendedor": 37,
			"codigo_personalizado": "",
			"apelido_vendedor": "CHEILA",
			"nome_vendedor": "ARISTEA CHEILA REIS DE OLIVEIRA"
		}, {
			"codigo_vendedor": 690,
			"codigo_personalizado": "",
			"apelido_vendedor": "CLELIA",
			"nome_vendedor": "CLELIA PEREIRA DA SILVA"
		}, {
			"codigo_vendedor": 73,
			"codigo_personalizado": "",
			"apelido_vendedor": "DANIELA",
			"nome_vendedor": "DANIELA FERREIRA PEREIRA"
		}, {
			"codigo_vendedor": 546,
			"codigo_personalizado": "",
			"apelido_vendedor": "DAYSE",
			"nome_vendedor": "DAYSE RODRIGUES CABRAL ELIAS"
		}, {
			"codigo_vendedor": 80,
			"codigo_personalizado": "",
			"apelido_vendedor": "DEYSE",
			"nome_vendedor": "NAENE CALAZANS DA SILVA"
		}, {
			"codigo_vendedor": 136,
			"codigo_personalizado": "",
			"apelido_vendedor": "DIEGO",
			"nome_vendedor": "DIEGO HENRIQUE GOMES"
		}, {
			"codigo_vendedor": 547,
			"codigo_personalizado": "",
			"apelido_vendedor": "DIEGO",
			"nome_vendedor": "DIEGO HENRIQUE GOMES FARIAS"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
	"listar_vendedores": {
		"status": 0,
		"mensagem": "",
		"vendedores": []
	}
}


```

_**Resposta de erro:**_

```json
{
	"listar_vendedores": {
		"status": 1,
		"mensagem": "Informe o código do usuário"
	}
}
{
	"listar_vendedores": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Listar Empresas

Lista todas as empresas que o usuário logado tem acesso, para escolher numa combo de filtro a empresa desejada

_**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_empresas": {
		"cod_usuario": "209",
		"chave": "05FE6359-DB53-1D2B-0840-6C84B3CA25AC"
	}
}"
```

_**Resposta de sucesso:**_

```json
{
	"listar_empresas": {
		"status": 0,
		"mensagem": "",
		"empresas": [{
			"codigo_empresa": 20,
			"nome_empresa": "ABC FLORESTAL"
		}, {
			"codigo_empresa": 2,
			"nome_empresa": "DDIEX"
		}, {
			"codigo_empresa": 19,
			"nome_empresa": "LOGOS"
		}, {
			"codigo_empresa": 1,
			"nome_empresa": "PAPELARIA ABC"
		}, {
			"codigo_empresa": 3,
			"nome_empresa": "TELEVENDAS"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
	"listar_empresas": {
		"status": 0,
		"mensagem": "",
		"empresas": []
	}
}
```

_**Resposta de erro:**_

```json
{
	"listar_empresas": {
		"status": 1,
		"mensagem": "Informe o código do usuário"
	}
}
{
	"listar_empresas": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Listar Situações da Venda

Lista todas as situações da venda que o usuário logado tem acesso, para escolher numa combo de filtro a situação desejada

_**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_situacoes_venda": {
		"chave": "05FE6359-DB53-1D2B-0840-6C84B3CA25AC"
	}
}"
```

_**Resposta de sucesso:**_

```json
{
	"listar_situacoes_venda": {
		"status": 0,
		"mensagem": "",
		"situacoes": [{
			"codigo_situacao": 0,
			"nome_situacao": "Criada no Caixa",
			"cor_situacao": "#036380"
		}, {
			"codigo_situacao": 1,
			"nome_situacao": "Enviado para o Caixa",
			"cor_situacao": "#f7941d"
		}, {
			"codigo_situacao": 2,
			"nome_situacao": "Pré Venda Cancelada",
			"cor_situacao": "#ca232b"
		}, {
			"codigo_situacao": 3,
			"nome_situacao": "Pendente",
			"cor_situacao": "#959595"
		}, {
			"codigo_situacao": 4,
			"nome_situacao": "Cliente Desistiu",
			"cor_situacao": "#8d181e"
		}, {
			"codigo_situacao": 5,
			"nome_situacao": "Finalizada",
			"cor_situacao": "#8cc739"
		}, {
			"codigo_situacao": 6,
			"nome_situacao": "Orçamento Recusado",
			"cor_situacao": "#537da4"
		}, {
			"codigo_situacao": 7,
			"nome_situacao": "Pendente de negociação",
			"cor_situacao": "#c69c6d"
		}, {
			"codigo_situacao": 8,
			"nome_situacao": "Retornou para a pré venda",
			"cor_situacao": "#047680"
		}, {
			"codigo_situacao": 9,
			"nome_situacao": "Pré-Venda Removida",
			"cor_situacao": "#363636"
		}, {
			"codigo_situacao": 10,
			"nome_situacao": "Pendente de Verificação",
			"cor_situacao": "#959595"
		}, {
			"codigo_situacao": 11,
			"nome_situacao": "Pedido Aprovado",
			"cor_situacao": "#047680"
		}, {
			"codigo_situacao": 12,
			"nome_situacao": "Liberado para Envio",
			"cor_situacao": "#2584ee"
		}, {
			"codigo_situacao": 13,
			"nome_situacao": "Enviado ao Servidor",
			"cor_situacao": "#8cc739"
		}, {
			"codigo_situacao": 14,
			"nome_situacao": "Confirmado",
			"cor_situacao": "#ca232b"
		}, {
			"codigo_situacao": 15,
			"nome_situacao": "Cancelado Pelo Cliente",
			"cor_situacao": "#ca232b"
		}, {
			"codigo_situacao": 16,
			"nome_situacao": "Cancelado Pela Loja",
			"cor_situacao": "#8d181e"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
	"listar_situacoes_venda": {
		"status": 0,
		"mensagem": "",
		"situacoes": []
	}
}
```

_**Resposta de erro:**_

```json
{
	"listar_situacoes_venda": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```



### Listar Grupos

Lista todos os grupos, para escolher numa combo de filtro.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_grupos_prod": {
        "chave": "05FE6359-DB53-1D2B-0840-6C84B3CA25AC"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_grupos_prod": {
		"status": 0,
		"mensagem": "",
		"grupos": [{
			"cod_grupo": 64,
			"nome_grupo": "70% DESCONTO"
		}, {
			"cod_grupo": 40,
			"nome_grupo": "ACESSORIOS DE INFORMATICA"
		}, {
			"cod_grupo": 55,
			"nome_grupo": "ACESSORIOS PARA NOTEBOOK"
		}, {
			"cod_grupo": 54,
			"nome_grupo": "ADAPTADORES E HUBS"
		}, {
			"cod_grupo": 23,
			"nome_grupo": "AGENDAS"
		}, {
			"cod_grupo": 27,
			"nome_grupo": "ALIMENTOS"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_grupos_prod": {
        "status": 0,
        "mensagem": "",
        "grupos": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_grupos_prod": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```



### Listar Marcas

Lista todos as marcas, para escolher numa combo de filtro.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_marcas": {
        "chave": "05FE6359-DB53-1D2B-0840-6C84B3CA25AC"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_marcas": {
		"status": 0,
		"mensagem": "",
		"marcas": [{
			"codigo_marcca": 752,
			"nome_marca": "0"
		}, {
			"codigo_marcca": 374,
			"nome_marca": "3 CORACOES"
		}, {
			"codigo_marcca": 962,
			"nome_marca": "3D EDITORA"
		}, {
			"codigo_marcca": 38,
			"nome_marca": "3M"
		}, {
			"codigo_marcca": 732,
			"nome_marca": "7 BELO"
		}, {
			"codigo_marcca": 950,
			"nome_marca": "ABACATE"
		}, {
			"codigo_marcca": 22,
			"nome_marca": "ABC"
		}, {
			"codigo_marcca": 34,
			"nome_marca": "ACC"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_marcas": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_marcas": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Listar Departamentos

Lista todos os departamentos, para escolher numa combo de filtro.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_departamentos": {
        "chave": "05FE6359-DB53-1D2B-0840-6C84B3CA25AC"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_departamentos": {
		"status": 0,
		"mensagem": "",
		"departamentos": [{
			"codigo_departamento": 11,
			"nome_departamento": "ADAPTADORES E HUBS"
		}, {
			"codigo_departamento": 9,
			"nome_departamento": "BAZAR"
		}, {
			"codigo_departamento": 17,
			"nome_departamento": "CID ARTES"
		}, {
			"codigo_departamento": 6,
			"nome_departamento": "DIVERSAO"
		}, {
			"codigo_departamento": 15,
			"nome_departamento": "FRETE"
		}, {
			"codigo_departamento": 4,
			"nome_departamento": "LEITURA"
		}, {
			"codigo_departamento": 19,
			"nome_departamento": "MAGNA CART"
		}, {
			"codigo_departamento": 5,
			"nome_departamento": "MERCEARIA E LIMPEZA"
		}, {
			"codigo_departamento": 7,
			"nome_departamento": "MOVEIS"
		}, {
			"codigo_departamento": 10,
			"nome_departamento": "N/D"
		}, {
			"codigo_departamento": 8,
			"nome_departamento": "PAPEL"
		}, {
			"codigo_departamento": 3,
			"nome_departamento": "PAPELARIA"
		}, {
			"codigo_departamento": 2,
			"nome_departamento": "TECNOLOGIA"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_departamentos": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_departamentos": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Listar Estados

Lista todos os estados, para escolher numa combo de filtro.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_estados": {
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_estados": {
		"status": 0,
		"mensagem": "",
		"estados": [{
			"codigo_estado": 1,
			"sigla_uf": "Acre"
		}, {
			"codigo_estado": 2,
			"sigla_uf": "Alagoas"
		}, {
			"codigo_estado": 4,
			"sigla_uf": "Amazonas"
		}, {
			"codigo_estado": 3,
			"sigla_uf": "Amapá"
		}, {
			"codigo_estado": 5,
			"sigla_uf": "Bahia"
		}, {
			"codigo_estado": 6,
			"sigla_uf": "Ceará"
		}, {
			"codigo_estado": 7,
			"sigla_uf": "Distrito Federal"
		}, {
			"codigo_estado": 8,
			"sigla_uf": "Espirito Santo"
		}, {
			"codigo_estado": 9,
			"sigla_uf": "Goiás"
		}, {
			"codigo_estado": 10,
			"sigla_uf": "Maranhão"
		}, {
			"codigo_estado": 12,
			"sigla_uf": "Minas Gerais"
		}, {
			"codigo_estado": 11,
			"sigla_uf": "Mato Grosso do Sul"
		}, {
			"codigo_estado": 27,
			"sigla_uf": "Mato Grosso"
		}, {
			"codigo_estado": 13,
			"sigla_uf": "Pará"
		}, {
			"codigo_estado": 14,
			"sigla_uf": "Paraíba"
		}, {
			"codigo_estado": 16,
			"sigla_uf": "Pernambuco"
		}, {
			"codigo_estado": 17,
			"sigla_uf": "Piauí"
		}, {
			"codigo_estado": 15,
			"sigla_uf": "Paraná"
		}, {
			"codigo_estado": 18,
			"sigla_uf": "Rio de Janeiro"
		}, {
			"codigo_estado": 19,
			"sigla_uf": "Rio Grande do Norte"
		}, {
			"codigo_estado": 21,
			"sigla_uf": "Rondônia"
		}, {
			"codigo_estado": 22,
			"sigla_uf": "Roraima"
		}, {
			"codigo_estado": 20,
			"sigla_uf": "Rio Grande do Sul"
		}, {
			"codigo_estado": 23,
			"sigla_uf": "Santa Catarina"
		}, {
			"codigo_estado": 25,
			"sigla_uf": "Sergipe"
		}, {
			"codigo_estado": 24,
			"sigla_uf": "São Paulo"
		}, {
			"codigo_estado": 26,
			"sigla_uf": "Tocantins"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_estados": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_estados": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Listar Perfis

Lista todos os perfis, para escolher numa combo de filtro.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_perfis": {
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_perfis": {
		"status": 0,
		"mensagem": "",
		"perfis": [{
			"codigo_perfil": 3,
			"descricao_perfil": "DDIEX"
		}, {
			"codigo_perfil": 6,
			"descricao_perfil": "FUNCIONARIO ABC"
		}, {
			"codigo_perfil": 1,
			"descricao_perfil": "LOJA ABC"
		}, {
			"codigo_perfil": 5,
			"descricao_perfil": "LegisClub"
		}, {
			"codigo_perfil": 4,
			"descricao_perfil": "MarktClub"
		}, {
			"codigo_perfil": 2,
			"descricao_perfil": "TELEVENDAS"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_perfis": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_perfis": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Consultar Escola

A consulta de escola é uma das etapas para consultar a lista de material. Primeiro será chamado a consulta de escola, logo depois a consulta de séries e a consulta dos itens da lista.



**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_escolas": {
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_escolas": {
		"status": 0,
		"mensagem": "",
		"escolas": [{
			"codigo_escola": 102,
			"nome_escola": "AFFINITY ARTS - INTERNATIONAL SCHOOL"
		}, {
			"codigo_escola": 127,
			"nome_escola": "APTA - BERÇÁRIO E EDUCAÇÃO INFANTIL"
		}, {
			"codigo_escola": 139,
			"nome_escola": "ASSOCIACAO NOSSA SENHORA DA DIVINA PROVIDENCIA"
		}, {
			"codigo_escola": 22,
			"nome_escola": "CECAN"
		}, {
			"codigo_escola": 28,
			"nome_escola": "CEMA - CENTRO EDUCACIONAL MARIA AUXILIADORA"
		}, {
			"codigo_escola": 172,
			"nome_escola": "CENEB"
		}, {
			"codigo_escola": 158,
			"nome_escola": "CENTRO DE ENSINO DA MONICA"
		}, {
			"codigo_escola": 126,
			"nome_escola": "CENTRO DE ENSINO ESPAÇO DO SABER"
		}, {
			"codigo_escola": 20,
			"nome_escola": "CENTRO EDUCACIONAL CATÓLICA DE BRASILIA"
		}, {
			"codigo_escola": 24,
			"nome_escola": "CENTRO EDUCACIONAL LEONARDO DA VINCI"
		}, {
			"codigo_escola": 104,
			"nome_escola": "CENTRO EDUCACIONAL RENASCENCA"
		}, {
			"codigo_escola": 135,
			"nome_escola": "CENTRO EDUCACIONAL VICENTE PIRES"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_escolas": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_escolas": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Consultar Séries

A consulta de séries é a segunda etapa para consultar a lista de material. Primeiro será chamado a consulta de escola, logo depois a consulta de séries e a consulta dos itens da lista.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_series": {
        "codigo_escola":"20",
        "codigo_empresa":"1",
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
"
```

**\*Resposta de sucesso:***

```json
{
	"listar_series": {
		"status": 0,
		"mensagem": "",
		"series": [{
			"codigo_lista": 2729,
			"codigo_escola": 20,
			"codigo_serie": 169,
			"data_hora_cadastro": "24/11/2017 17:14",
			"ultima_atualizacao": "14/01/2018 14:38",
			"escola": "CENTRO EDUCACIONAL CATÓLICA DE BRASILIA",
			"serie": "1 ANO",
			"quantidade_total": "48",
			"valor_total": "811,46",
			"observacao": "ITENS NÃO COTADOS:\n\n- MOCHILA\n\n- LIVRO:   A ÁRVORE DOS MEUS DOIS QUINTAIS  \n\n  ORÇAMENTO VÁLIDO SOMENTE POR UM DIA. \n\n ACOMPANHE O ANDAMENTO DO SEU VALE LIVRO EM:\n\nHTTP://VALELIVRO.ABCLOJA.COM.BR:9004/VALE"
		}, {
			"codigo_lista": 2721,
			"codigo_escola": 20,
			"codigo_serie": 24,
			"data_hora_cadastro": "24/11/2017 15:19",
			"ultima_atualizacao": "24/11/2017 16:46",
			"escola": "CENTRO EDUCACIONAL CATÓLICA DE BRASILIA",
			"serie": "1 ANO MEDIO",
			"quantidade_total": "18",
			"valor_total": "2.622,31",
			"observacao": "ORÇAMENTO VÁLIDO SOMENTE POR UM DIA  ORÇAMENTO VÁLIDO SOMENTE POR UM DIA.  ACOMPANHE O ANDAMENTO DO SEU VALE LIVRO EM:\n\nHTTP://VALELIVRO.ABCLOJA.COM.BR:9004/VALE"
		}, {
			"codigo_lista": 2730,
			"codigo_escola": 20,
			"codigo_serie": 170,
			"data_hora_cadastro": "24/11/2017 17:41",
			"ultima_atualizacao": "14/01/2018 14:38",
			"escola": "CENTRO EDUCACIONAL CATÓLICA DE BRASILIA",
			"serie": "2 ANO",
			"quantidade_total": "60",
			"valor_total": "1.378,84",
			"observacao": "ITENS NÃO COTADOS:\n\n- BLOCO PRODUÇÃO DE TEXTO PADRÃO\n- ESTOJO\n- CAIXA DE SAPATO\n- TAMPINHAS DE REFRIGERANTE\n\n\n  ORÇAMENTO VÁLIDO SOMENTE POR UM DIA .  \n\n\nACOMPANHE O ANDAMENTO DO SEU VALE LIVRO EM:   HTTP://VALELIVRO.ABCLOJA.COM.BR:9004/VALE"
		}, {
			"codigo_lista": 2727,
			"codigo_escola": 20,
			"codigo_serie": 25,
			"data_hora_cadastro": "24/11/2017 16:35",
			"ultima_atualizacao": "14/12/2017 17:24",
			"escola": "CENTRO EDUCACIONAL CATÓLICA DE BRASILIA",
			"serie": "2 ANO MEDIO",
			"quantidade_total": "16",
			"valor_total": "2.666,93",
			"observacao": "ORÇAMENTO VÁLIDO SOMENTE POR UM DIA  ORÇAMENTO VÁLIDO SOMENTE POR UM DIA.\n\nItens não cotados:\n\nJuca Pirama\nIracema\nMemorias Postumas de Brás Cubas\nCortiço.  ACOMPANHE O ANDAMENTO DO SEU VALE LIVRO EM:\n\nHTTP://VALELIVRO.ABCLOJA.COM.BR:9004/VALE"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_series": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_series": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Consultar Produtos da Lista

A consulta dos produtos da lista é a última etapa para consultar a lista de material. Primeiro será chamado a consulta de escola, logo depois a consulta de séries e a consulta dos itens da lista.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "produtos_lista": {
        "codigo_lista":"2721",
        "codigo_empresa":"1",
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
"
```

**\*Resposta de sucesso:***

```json
{
	"produtos_lista": {
		"status": 0,
		"mensagem": "",
		"produtos_lista": [{
			"codigo_lista": 2721,
			"codigo_item_lista": 62340,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4010710,
			"nome_produto": "360º  GRAMATICA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "239,01",
			"valor_total": "239,01"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62516,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4018478,
			"nome_produto": "360º GEOGRAFIA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "239,00",
			"valor_total": "239,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62571,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4011830,
			"nome_produto": "360º HISTORIA  EDITORA FTD",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "239,00",
			"valor_total": "239,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62519,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 557269,
			"nome_produto": "ACHIEVE 1 STUDENTBOOK E WORKBOOK 2 EDICAO OXFORD",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "155,00",
			"valor_total": "155,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62524,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4077381,
			"nome_produto": "BARACK OBAMA\nMODERNA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "46,00",
			"valor_total": "46,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62518,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4089433,
			"nome_produto": "BIOLOGIA VOLUME UNICO (SONIA LOPES)SARAIVA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "253,00",
			"valor_total": "253,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62537,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 819182,
			"nome_produto": "CENA EM SALA ENSINO MEDIO ED.HTC VOL.01",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "131,00",
			"valor_total": "131,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62530,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 994030,
			"nome_produto": "DIALOGO PRIMEIROS EST EM FILMODERNA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "168,00",
			"valor_total": "168,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62562,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4091242,
			"nome_produto": "LITERATURA SER PROTAGONISTA BOX UNICO EDITORA SM",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "140,00",
			"valor_total": "140,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62522,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4090741,
			"nome_produto": "MALALA ED. RICHMOND",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "40,00",
			"valor_total": "40,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62368,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 41122,
			"nome_produto": "MARILIA DE DIRCEU ED.L&PM",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "16,90",
			"valor_total": "16,90"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62369,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 971618,
			"nome_produto": "MATEMATICA VOLUME UNICO (GELSON IEZZI) ATUAL",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "219,00",
			"valor_total": "219,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62527,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 198676,
			"nome_produto": "MINIDICIONARIO INGPOR/PORINGS.BUENOCM2007",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "55,00",
			"valor_total": "55,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62517,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 567868,
			"nome_produto": "MODERNA PLUS FISICA 1MODERNA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "220,00",
			"valor_total": "220,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62365,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 681849,
			"nome_produto": "OS LUSIADAS COL. CLASSICOS SARAIVA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "35,50",
			"valor_total": "35,50"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62515,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4080069,
			"nome_produto": "PROJETO MULTIPLO - QUIMICA 1ATICA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "229,00",
			"valor_total": "229,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62535,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4076435,
			"nome_produto": "SOCIEDADE INTRODUCAO CIENCIAS DA SOCIEDADE 5 EDICAO MODERNA",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "180,00",
			"valor_total": "180,00"
		}, {
			"codigo_lista": 2721,
			"codigo_item_lista": 62352,
			"codigo_grupo_lista": 3,
			"grupo_lista": "Livros",
			"codigo_produto": 4091240,
			"nome_produto": "SONHO DE UMA NOITE DE VERAO LPM",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"quantidade": "1",
			"valor_venda": "16,90",
			"valor_total": "16,90"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "produtos_lista": {
        "status": 0,
        "mensagem": "",
        "marcas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"produtos_lista": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Processar Produto

Esta função será utilizado tanto para consultas de produtos quanto para gravação de produtos em uma venda.

**codigo_empresa:** informa o código da empresa do funcionário logado

**produto:** Sera enviado pelo sistema sendo numerico ou string, ou seja, pode ser enviado o código do produto ou o nome do produto para realizar a pesquisa ou gravação.

**utiliza_mix**: Campo utilizado para informar se a pesquisa ou gravação será realizada dentro do cardápio. Informação recuperada do serviço de autenticação

**config_possui_lote:** esta configuração faz com que a busca pelo produto aconteça utilizando o código do lote. parâmetro vindo do serviço de autenticação

**possui_estoque e possui_promocao:** não serão utilizadas no momento, pode enviar 'N'

**opcao_gravacao:** Informar se a ação será de gravação ou de consulta
1: Gravação na tabela de item da venda
Nulo ou Zero: não realiza gravação, somente busca os dados do produto. Caso seja informado a opção de gravação, a procedure irá buscar o produto e caso encontre o produto irá realizar o procedimento de gravar os dados na tabela de item da venda.

Caso informe a função de gravar os dados na tabela de item da venda será necessário informar as seguintes variaveis de entrada:

- codigo_funcionario
- nome_funcionario
- codigo_venda
- quantidade de itens para gravar
- observacao

**totalizar_itens:**Indica que após a gravação do produto na tabela de itens da venda a procedure irá totalizar a soma dos produtos e atualizar a tabela de venda e retornar os totais da venda no json de retorno

SOMENTE QUANDO O PARÂMETRO totalizar_itens FOR INFORMADO 'S' será retornado as seguintes variaveis abaixo:
--subtotal
--total_desconto
--total_acrescimos
--total_final
--quantidade_total
--total_cashback
--total_servico

**acumula_item:**Esse parâmetro faz com que o sistema some os valores e quantidade caso já existe o produto lançado na tabela de item da venda. parâmetro vindo do serviço de autenticação

**critica_por_func=**Este parâmetro valida se o produto já existe na tabela de item da venda pelo código do produto e pelo funcionário que está lançando. Isso faz com que a comissão seja dividido entre os vendedores de acordo com o que ele lança no sistema. parâmetro vindo do serviço de autenticação

**utiliza_balanca:** informa se o calculo da quantidade do produto será realizado pelo valor recuperado da etiqueta da balança dividido pelo valor de vendo do produto. Neste caso, quando for S nesse campo obrigatoriamente deve existir um valor no campo valor_balanca. parâmetro vindo do serviço de autenticação



***Requisição:\***

```json
POST /execForcaVendas.rule?sys=GFS&json="
EXEMPLO DE UMA PESQUISA PELO CÓDIGO DE BARRAS DE UM PRODUTO
{
	"processa_produto": {
		"codigo_empresa": "1",
		"produto": "7898943398741",
		"utiliza_mix": "N",
		"config_possui_lote": "N",
		"possui_estoque": "N",
		"possui_promocao": "N",
		"opcao_gravacao": "0",
		"totalizar_itens": "N",
		"codigo_funcionario": "58",
		"nome_funcionario": "CAROLINA",
		"codigo_venda": "0",
		"quantidade": "0",
		"observacao": "",
		"acumula_item": "S",
		"critica_por_func": "N",
		"utiliza_balanca": "N",
		"valor_balanca": "0",
		"cod_lote": "0",
		"codigo_perfil": "1",
		"preco_diferenciado": "N",
		"incide_servico": "N",
		"chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
	}
}

EXEMPLO DE UMA CHAMADA PARA GRAVAR O PRODUTO NA VENDA, TOTALIZANDO A VENDA
{
	"processa_produto": {
		"codigo_empresa": "1",
		"produto": "7898943398741",
		"utiliza_mix": "N",
		"config_possui_lote": "N",
		"possui_estoque": "N",
		"possui_promocao": "N",
		"opcao_gravacao": "1",
		"totalizar_itens": "S",
		"codigo_funcionario": "58",
		"nome_funcionario": "CAROLINA",
		"codigo_venda": "168645",
		"quantidade": "1",
		"observacao": "",
		"acumula_item": "S",
		"critica_por_func": "N",
		"utiliza_balanca": "N",
		"valor_balanca": "0",
		"cod_lote": "0",
		"codigo_perfil": "1",
		"preco_diferenciado": "N",
		"incide_servico": "N",
		"chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
	}
}
"
```

***Resposta de sucesso:\***

```json
EXEMPLO DE RETORNO DE UMA PESQUISA DE PRODUTOS PELO NOME
{
	"processa_produto": {
		"status": 0,
		"mensagem": "",
		"totaliza_venda": {},
		"produtos": [{
			"codigo_produto": 4085638,
			"perc_minimo": 0.00,
			"perc_maximo": 5.00,
			"cod_barras": "978110748601",
			"nome_produto": "EYES OPEN 1 SB A W/ONLINE WB\nCAMBRIGDE",
			"possui_lote": "N",
			"valor_venda": "164,00",
			"valor_compra": "119,72",
			"valor_custo": "119,72",
			"opcao_fracao": "N",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"incide_servico": "N",
			"codigo_grupo": 39,
			"grupo": "LIVROS E REVISTAS",
			"url_imagem": "",
			"cod_promocao": 0,
			"cod_lote": 0,
			"cod_barras_lote": "",
			"cod_ref_lote": "",
			"nome_lote": ""
		}, {
			"codigo_produto": 4086559,
			"perc_minimo": 0.00,
			"perc_maximo": 5.00,
			"cod_barras": "9781107486041",
			"nome_produto": "EYES OPEN 1 SB B W/ONLINE WB\nCAMBRIGDE",
			"possui_lote": "N",
			"valor_venda": "164,00",
			"valor_compra": "119,72",
			"valor_custo": "119,72",
			"opcao_fracao": "N",
			"codigo_unidade": 2,
			"sigla_unidade": "UN",
			"incide_servico": "N",
			"codigo_grupo": 39,
			"grupo": "LIVROS E REVISTAS",
			"url_imagem": "",
			"cod_promocao": 0,
			"cod_lote": 0,
			"cod_barras_lote": "",
			"cod_ref_lote": "",
			"nome_lote": ""
		}]
	}
}

EXEMPLO DE UM RETORNO DE GRAVAÇÃO DE UM PRODUTO
{  
   "processa_produto":{  
      "status":0,
      "mensagem":"",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168645,
         "quantidade_total":"5",
         "subtotal":"399,50",
         "total_desconto":"0,00",
         "total_acrescimos":"0,00",
         "total_final":"399,50",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },
      "itens_venda":[  
         {  
            "codigo_item_venda":1158579,
            "codigo_produto":1005308,
            "codigo_personalizado":"",
            "codigo_barras":"7898943398741",
            "codigo_apresentacao":"1005308",
            "nome_produto":"RADIO PORTATIL LENDEX FM C/ENT S/USB LD-CS32",
            "sigla_unidade":"UN",
            "quantidade_itens":"5",
            "valor_venda":"79,90",
            "valor_desconto":"0,00",
            "total_produto":"399,50",
            "data_hora_cadastro":"13/09/2018 17:54",
            "hora_cadastro":"17:54",
            "vendedor_item":"LIZANDRA",
            "observacao":""
         }
      ],
      "produtos":[  
         {  
            "codigo_produto":1005308,
            "perc_minimo":0.00,
            "perc_maximo":5.00,
            "cod_barras":"7898943398741",
            "nome_produto":"RADIO PORTATIL LENDEX FM C/ENT S/USB LD-CS32",
            "possui_lote":"N",
            "valor_venda":"79,90",
            "valor_compra":"35,81",
            "valor_custo":"45,96",
            "opcao_fracao":"N",
            "codigo_unidade":2,
            "sigla_unidade":"UN",
            "incide_servico":"N",
            "codigo_grupo":46,
            "grupo":"AUDIO E VIDEO",
            "url_imagem":"",
            "cod_promocao":0,
            "codigo_cardapio":0,
            "cod_lote":0,
            "cod_barras_lote":"",
            "cod_ref_lote":"",
            "nome_lote":""
         }
      ]
   }
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
	"processa_produto": {
		"status": 1,
		"mensagem": "Produto não encontrado"
	}
}
```

***Resposta de erro:\***

```json
{
    "processa_produto": {
        "status": 1,
        "mensagem": "Informe o token de autorização"
    }
}
```

### Processa Novo Pedido

Esta função irá realizar a gravação de um novo pedido para iniciar uma venda. Os seguintes campos são obrigatórios para iniciar uma venda: codigo da empresa, codigo do vendedor, codigo do cliente, nome do cliente e perfil do cliente.

**codigo_empresa:** informa o código da empresa do funcionário logado recuperado no serviço de autenticação

**codigo_funcionario:** Sera enviado o código do funcionario recuperado no serviço de autenticação

**nome_funcionario:** Sera enviado o nome do funcionario recuperado no serviço de autenticação

**nome_usuario:** Sera enviado o nome do usuario recuperado no serviço de autenticação

**observacao_padrao:** Sera enviado a observação padrão recuperada no serviço de autenticação

**nome_orcamento:** Sera enviado o nome do orçamento padrão recuperado no serviço de autenticação

**config_id_pag_nfe:** Sera enviado o ig pag nfe padrão recuperado no serviço de autenticação

**nome_empresa:** Sera enviado o nome da empresa recuperado no serviço de autenticação

**possui_servico:** Sera enviado se trabalha com serviço. parâmetro recuperado no serviço de autenticação

**codigo_cliente:** Por padrão quando se inicia uma nova venda, será passado 1

**nome_cliente:** Por padrão quando se inicia uma nova venda, será passado 'CONSUMIDOR FINAL'

**codigo_natureza: **Por padrão quando se inicia uma nova venda, será passado 1

**codigo_perfil:** Por padrão quando se inicia uma nova venda, será passado 1



***Requisição:\***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"processa_novo_pedido": {
		"codigo_empresa": "1",
		"nome_empresa": "PAPELARIA ABC",
		"codigo_funcionario": "58",
		"nome_funcionario": "SUPORTE",
		"nome_usuario": "master",
		"codigo_natureza": "1",
		"codigo_cliente": "1",
		"nome_cliente": "CONSUMIDOR FINAL",
		"cpf_cnpj": "",
		"codigo_perfil": "1",
		"possui_servico": "N",
		"observacao_padrao": "VALIDADE DA PROPOSTA: 07 DIAS",
		"nome_orcamento": "ORÇAMENTO",
		"config_id_pag_nfe": "0",
		"chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
	}
}	
"
```

***Resposta de sucesso:\***

```json
{
	"processa_novo_pedido": {
		"status": 0,
		"mensagem": "",
		"codigo_funcionario": 58,
		"apelido_funcionario": "SUPORTE",
		"codigo_empresa": 1,
		"apelido_empresa": "PAPELARIA ABC",
		"codigo_venda": 168647,
		"codigo_mesa": 0,
		"codigo_sit_mesa": 0,
		"situacao_mesa": "",
		"dados_abertura": "29/05/2018 00:11",
		"codigo_cliente": 1,
		"nr_cpf_cnpj": "",
		"nome_cliente": "CONSUMIDOR FINAL",
		"subtotal": "0,00",
		"total_desconto": "0,00",
		"total_cashback": "0,00",
		"taxa_entrega": "0,00",
		"total_acrescimos": "0,00",
		"total_servico": "0,00",
		"quantidade_total": "0",
		"total_geral": "0,00"
	}
}
```

***Resposta de erro:\***

```json
{
    "processa_novo_pedido": {
        "status": 1,
        "mensagem": "Informe o token de autorização"
    }
}
```

### Listar Natureza

Lista todas as naturezas, para escolher numa combo.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_natureza": {
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_natureza": {
		"status": 0,
		"mensagem": "",
		"naturezas": [{
			"codigo_natureza": 2,
			"nome_natureza": "1102 - Compra para comercialização."
		}, {
			"codigo_natureza": 8,
			"nome_natureza": "1111 - Compra para industrialização  em consignação industrial"
		}, {
			"codigo_natureza": 9,
			"nome_natureza": "1113 - Compra para comercialização em consignação mercantil"
		}, {
			"codigo_natureza": 10,
			"nome_natureza": "1116 - Compra para industrialização ou produção para recebimento"
		}, {
			"codigo_natureza": 11,
			"nome_natureza": "1117 - Compra para comercialização originada de encomenda"
		}, {
			"codigo_natureza": 12,
			"nome_natureza": "1118 - Compra de mercadoria para comercialização pelo adquirente"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_natureza": {
        "status": 0,
        "mensagem": "",
        "naturezas": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_natureza": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### 

### Listar ibge

Lista os ibges, a listagem será no máximo de 100 registros, então deve existir a possibilidade do usuário realizar um filtro, informando o código do ibge ou a descrição.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "listar_ibge": {
      "codigo_ibge":"0",
      "nome_ibge":"ESPIRITO SANTO",
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"listar_ibge": {
		"status": 0,
		"mensagem": "",
		"ibges": [{
			"codigo_ibge": 3124401,
			"descricao": "MG - ESPIRITO SANTO DO DO"
		}, {
			"codigo_ibge": 2403509,
			"descricao": "RN - ESPIRITO SANTO"
		}, {
			"codigo_ibge": 3515186,
			"descricao": "SP - ESPIRITO SANTO DO PI"
		}, {
			"codigo_ibge": 3515194,
			"descricao": "SP - ESPIRITO SANTO DO TU"
		}]
	}
}

ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS
{
    "listar_ibge": {
        "status": 0,
        "mensagem": "",
        "ibges": []
    }
}
```

**\*Resposta de erro:***

```json
{
	"listar_ibge": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}
```

### Buscar CNPJ

Neste serviço será enviado o CNPJ para consulta na receita federal dos dados da empresa.



**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
    "buscar_cnpj": {
      "cnpj":"06787718000156",
        "chave": "75CEB695-5344-F0EE-C0E9-835F26C91D8B"
    }
}"
```

**\*Resposta de sucesso:***

```json
{
	"buscar_cnpj": {
		"status": "0",
		"mensagem": "",
		"nome_cliente": "TECFF TECNOLOGIA EM SOFTWARE EIRELI",
		"fantasia": "TECFF TECNOLOGIA",
		"cep": "71925000",
		"logradouro": "Q 205",
		"numero": ".",
		"complemento": "LOTE 01 SALAS 505 E 506 EDIF QUARTIER CENTER",
		"bairro": "SUL (AGUAS CLARAS)",
		"cidade": "BRASILIA",
		"uf": "DF",
		"telefone": "6130211525",
		"email": "mario.lemos@tecff.com.br",
		"codigo_ibge": "5300108"
	}
}

```

**\*Resposta de erro:***

```json
{
	"buscar_cnpj": {
		"status": "1",
		"mensagem": "Houve uma falha na busca do CNPJ"
	}
}

{
	"buscar_cnpj": {
		"status": "1",
		"mensagem": "CNPJ inválido"
	}
}

{
	"buscar_cnpj": {
		"status": "1",
		"mensagem": "CNPJ rejeitado pela Receita Federal"
	}
}
```

### 

### Cadastrar Cliente

Esta função irá realizar a gravação de um novo cliente. Os seguintes campos são obrigatórios para gravar um cliente: codigo da empresa, codigo do vendedor, codigo do cliente, nome do cliente, celular, cpf, tipo da pessoa, no caso de PJ o nome fantasia e perfil do cliente. Campos que possuem algum tipo de tratamento expecífico ou listagem de dados estão descritos abaixo.

**codigo_funcionario:** Sera enviado o código do funcionario recuperado no serviço de autenticação

**nome_funcionario:** Sera enviado o nome do funcionario recuperado no serviço de autenticação

**nome_usuario:** Sera enviado o nome do usuario recuperado no serviço de autenticação

**codigo_empresa:** informa o código da empresa do funcionário logado recuperado no serviço de autenticação

**nome_cliente:** carregar com o nome digitado no app

**codigo_natureza: **Buscar a opção selecionada pelo usuario. Atraves da lista de perfis. (Serviço listar_natureza)

**codigo_perfil:** Buscar a opção selecionada pelo usuario. Atraves da lista de perfis. (Serviço listar_perfis)

**codigo_uf:** Buscar a opção selecionada pelo usuário. Através da lista de estados. (Serviço: listar_estados)

**codigo_ibge:** Buscar a opção selecionada pelo usuário. Através da lista de códigos ibges. (Serviço: listar_ibge)

**sexo:** presentar uma lista para escolha do usuário com as seguintes opções (Masculino, Feminino). Enviar para o serviço M ou F

**cep:** Este campo precisa ter a opção de realizar uma pesquisa pelo CEP e preencher os dados do endereço

**cnpj:** Este campo deve possuir um botão ao lado para que seja realizada uma busca dos dados do CNPJ informando, através do serviço (buscar_cnpj)

**contribuinte_icms:** apresentar uma lista para escolha do usuário com as seguintes opções (Por padrão deixe setado na opção 1):

1 - Contribuinte
2 - Isento
9 - Não Contribuinte

**enviar_email_nfe:** apresentar uma lista para escolha do usuário com as seguintes opções (Por padrão deixe setado na opção 1):

1 - Não Enviar
2 - Enviar Danfe
3 - Enviar XML
4 - Enviar XML/Danfe



***Requisição:\***

```json
POST /execForcaVendas.rule?sys=GFS&json="
EXEMPLO DE CADASTRO DE UM CLIENTE PESSOA FISICA
{
	"cadastra_cliente": {
		"codigo_funcionario": "58",
		"nome_funcionario": "SUPORTE",
		"nome_usuario": "GCOMWEB",
		"codigo_empresa": "1",

   		"tipo_pessoa": "1",
		"codigo_perfil": "1",      
		"nome_cliente": "TESTE DE INCLUSAO",      
		"telefone": "6130211525",
		"celular": "61996320102",
		"email": "contato@tecff.com.br",
		"niver_dia": "25",
		"niver_mes": "01",
		"sexo": "M",

		"rg": "",
		"cpf": "32299651837",

		"cnpj": "",
		"inscricao_estadual": "",
      	"nome_fantasia": "",
      
		"cep": "71925000",
		"endereco": "QUADRA 205 LT 01 SALA",
		"numero_end": "505",
		"complemento": "ED. QUARTIER CENTER",
		"bairro": "AGUAS CLARAS",
		"cidade": "BRASILIA",      
      	"codigo_uf": "7",
      
		"observacoes": "",
		"fone_nota": "61963025645",
		"codigo_natureza": "1",
		"codigo_ibge": "5300108",
		"contribuinte_icms": "1",
		"enviar_email_nfe": "1",
		"retem_csll": "",
		"retem_csll_perc": "",
		"retem_irrf": "",
		"retem_irrf_perc": "",
		"retem_pis": "",
		"retem_pis_perc": "",
		"retem_cofins": "",
		"retem_cofins_perc": "",
		"retem_iss": "",
		"retem_iss_perc": "",
		"retem_prev": "",
		"retem_prev_perc": "",
		"retem_outros": "",
      
		"chave": "25A51D2D-0205-7305-D0C6-BA2FC7BD2074"
	}
}

EXEMPLO DE CADASTRO DE PESSOA JURIDICA
{
	"cadastra_cliente": {
		"codigo_funcionario": "58",
		"nome_funcionario": "SUPORTE",
		"nome_usuario": "GCOMWEB",
		"codigo_empresa": "1",

   		"tipo_pessoa": "2",
		"codigo_perfil": "1",      
		"nome_cliente": "INCLUSAO DE CLIENTE PJ",      
		"telefone": "6130211525",
		"celular": "61996320102",
		"email": "contato@tecff.com.br",
		"niver_dia": "25",
		"niver_mes": "01",
		"sexo": "M",

		"rg": "",
		"cpf": "",

		"cnpj": "23621454000185",
		"inscricao_estadual": "",
      	"nome_fantasia": "NOME FANTASIA TESTE",
      
		"cep": "71925000",
		"endereco": "QUADRA 205 LT 01 SALA",
		"numero_end": "505",
		"complemento": "ED. QUARTIER CENTER",
		"bairro": "AGUAS CLARAS",
		"cidade": "BRASILIA",      
      	"codigo_uf": "7",
      
		"observacoes": "",
		"fone_nota": "61963025645",
		"codigo_natureza": "1",
		"codigo_ibge": "5300108",
		"contribuinte_icms": "1",
		"enviar_email_nfe": "1",
		"retem_csll": "",
		"retem_csll_perc": "",
		"retem_irrf": "",
		"retem_irrf_perc": "",
		"retem_pis": "",
		"retem_pis_perc": "",
		"retem_cofins": "",
		"retem_cofins_perc": "",
		"retem_iss": "",
		"retem_iss_perc": "",
		"retem_prev": "",
		"retem_prev_perc": "",
		"retem_outros": "",
      
		"chave": "25A51D2D-0205-7305-D0C6-BA2FC7BD2074"
	}
}

EXEMPLO DE CADASTRO COM PERCENTUAIS DE RETENÇÃO PARA PESSOA FISICA
{
	"cadastra_cliente": {
		"codigo_funcionario": "58",
		"nome_funcionario": "SUPORTE",
		"nome_usuario": "GCOMWEB",
		"codigo_empresa": "1",

   		"tipo_pessoa": "1",
		"codigo_perfil": "1",      
		"nome_cliente": "CLIENTE TESTE APP 5",      
		"telefone": "6130211525",
		"celular": "61996320102",
		"email": "contato@tecff.com.br",
		"niver_dia": "25",
		"niver_mes": "01",
		"sexo": "M",

		"rg": "",
		"cpf": "21894342210",

		"cnpj": "",
		"inscricao_estadual": "",
      	"nome_fantasia": "",
      
		"cep": "71925000",
		"endereco": "QUADRA 205 LT 01 SALA",
		"numero_end": "505",
		"complemento": "ED. QUARTIER CENTER",
		"bairro": "AGUAS CLARAS",
		"cidade": "BRASILIA",      
      	"codigo_uf": "7",
      
		"observacoes": "",
		"fone_nota": "61963025645",
		"codigo_natureza": "1",
		"codigo_ibge": "5300108",
		"contribuinte_icms": "1",
		"enviar_email_nfe": "1",
		"retem_csll": "S",
		"retem_csll_perc": "2",
		"retem_irrf": "S",
		"retem_irrf_perc": "3",
		"retem_pis": "S",
		"retem_pis_perc": "4",
		"retem_cofins": "S",
		"retem_cofins_perc": "5",
		"retem_iss": "S",
		"retem_iss_perc": "6",
		"retem_prev": "S",
		"retem_prev_perc": "7",
		"retem_outros": "S",
      
		"chave": "25A51D2D-0205-7305-D0C6-BA2FC7BD2074"
	}
}	
"
```

***Resposta de sucesso:\***

```json
{
	"cadastra_cliente": {
		"status": "0",
		"mensagem": "",
		"codigo_cliente": "100461",
		"cpf": "32299651837",
		"cnpj": "",
		"nome": "TESTE DE INCLUSAO"
	}
}

```

***Resposta de erro:\***

```json
{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o perfil"
	}
}

{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o tipo da pessoa"
	}
}

{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o cpf"
	}
}

{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o celular"
	}
}

{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o nome fantasia"
	}
}

{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o cnpj"
	}
}

{
	"cadastra_cliente": {
		"status": "1",
		"mensagem": "Informe o nome do cliente"
	}
}
```



### Atualizar Cliente

Esta função irá realizar a atualização de dados de um cliente existente. Será necessário informar obrigatoriamente o código do cliente para que o sistema possa realizar a alteração. Campos que possuem algum tipo de tratamento expecífico ou listagem de dados estão descritos abaixo.

**codigo_cliente:** Deve ser enviado o código do cliente em questão para realizar a alteração

**codigo_funcionario:** Sera enviado o código do funcionario recuperado no serviço de autenticação

**nome_funcionario:** Sera enviado o nome do funcionario recuperado no serviço de autenticação

**nome_usuario:** Sera enviado o nome do usuario recuperado no serviço de autenticação

**codigo_empresa:** informa o código da empresa do funcionário logado recuperado no serviço de autenticação

**nome_cliente:** carregar com o nome digitado no app

**codigo_natureza: **Buscar a opção selecionada pelo usuario. Atraves da lista de perfis. (Serviço listar_natureza)

**codigo_perfil:** Buscar a opção selecionada pelo usuario. Atraves da lista de perfis. (Serviço listar_perfis)

**codigo_uf:** Buscar a opção selecionada pelo usuário. Através da lista de estados. (Serviço: listar_estados)

**codigo_ibge:** Buscar a opção selecionada pelo usuário. Através da lista de códigos ibges. (Serviço: listar_ibge)

**sexo:** presentar uma lista para escolha do usuário com as seguintes opções (Masculino, Feminino). Enviar para o serviço M ou F

**cep:** Este campo precisa ter a opção de realizar uma pesquisa pelo CEP e preencher os dados do endereço

**cnpj:** Este campo deve possuir um botão ao lado para que seja realizada uma busca dos dados do CNPJ informando, através do serviço (buscar_cnpj)

**contribuinte_icms:** apresentar uma lista para escolha do usuário com as seguintes opções (Por padrão deixe setado na opção 1):

1 - Contribuinte
2 - Isento
9 - Não Contribuinte

**enviar_email_nfe:** apresentar uma lista para escolha do usuário com as seguintes opções (Por padrão deixe setado na opção 1):

1 - Não Enviar
2 - Enviar Danfe
3 - Enviar XML
4 - Enviar XML/Danfe



***Requisição:\***

```json
POST /execForcaVendas.rule?sys=GFS&json="
EXEMPLO DE ALTERAÇÃO DE UM CLIENTE PESSOA FISICA
{
	"atualiza_cliente": {
		"codigo_cliente": "100457",

   		"tipo_pessoa": "1",
		"codigo_perfil": "1",      
		"nome_cliente": "TESTE DE ALTERACAO DO CLIENTE",      
		"telefone": "6130211526",
		"celular": "61996320102",
		"email": "contato@tecff.com.br",
		"niver_dia": "25",
		"niver_mes": "01",
		"sexo": "M",

		"rg": "",
		"cpf": "32299651837",

		"cnpj": "",
		"inscricao_estadual": "",
      	"nome_fantasia": "",
      
		"cep": "71925000",
		"endereco": "QUADRA 205 LT 01 SALA",
		"numero_end": "505",
		"complemento": "ED. QUARTIER CENTER",
		"bairro": "AGUAS CLARAS",
		"cidade": "BRASILIA",      
      	"codigo_uf": "7",
      
		"observacoes": "",
		"fone_nota": "61963025645",
		"codigo_natureza": "1",
		"codigo_ibge": "5300108",
		"contribuinte_icms": "1",
		"enviar_email_nfe": "1",
		"retem_csll": "",
		"retem_csll_perc": "",
		"retem_irrf": "",
		"retem_irrf_perc": "",
		"retem_pis": "",
		"retem_pis_perc": "",
		"retem_cofins": "",
		"retem_cofins_perc": "",
		"retem_iss": "",
		"retem_iss_perc": "",
		"retem_prev": "",
		"retem_prev_perc": "",
		"retem_outros": "",
      
		"chave": "7AB55019-156A-1C9C-1EC6-06E156807915"
	}
}

EXEMPLO DE ALTERAÇÃO DE PESSOA JURIDICA
{
	"atualiza_cliente": {
		"codigo_cliente": "100462",

		"tipo_pessoa": "2",
		"codigo_perfil": "1",
		"nome_cliente": "ALTERACAO DE CLIENTE PJ",
		"telefone": "6130211525",
		"celular": "61996320102",
		"email": "contato@tecff.com.br",
		"niver_dia": "25",
		"niver_mes": "01",
		"sexo": "M",

		"rg": "",
		"cpf": "",

		"cnpj": "23621454000185",
		"inscricao_estadual": "",
		"nome_fantasia": "NOME FANTASIA TESTE",

		"cep": "71925000",
		"endereco": "QUADRA 205 LT 01 SALA",
		"numero_end": "505",
		"complemento": "ED. QUARTIER CENTER",
		"bairro": "AGUAS CLARAS",
		"cidade": "BRASILIA",
		"codigo_uf": "7",

		"observacoes": "",
		"fone_nota": "61963025645",
		"codigo_natureza": "1",
		"codigo_ibge": "5300108",
		"contribuinte_icms": "1",
		"enviar_email_nfe": "1",
		"retem_csll": "",
		"retem_csll_perc": "",
		"retem_irrf": "",
		"retem_irrf_perc": "",
		"retem_pis": "",
		"retem_pis_perc": "",
		"retem_cofins": "",
		"retem_cofins_perc": "",
		"retem_iss": "",
		"retem_iss_perc": "",
		"retem_prev": "",
		"retem_prev_perc": "",
		"retem_outros": "",

		"chave": "25A51D2D-0205-7305-D0C6-BA2FC7BD2074"
	}
}

EXEMPLO DE ATUALIZAÇÃO COM PERCENTUAIS DE RETENÇÃO PARA PESSOA FISICA
{
	"atualiza_cliente": {
		"codigo_cliente": "100459",

		"tipo_pessoa": "1",
		"codigo_perfil": "1",
		"nome_cliente": "TESTE ALTERACAO DE RETENCOES",
		"telefone": "6130211525",
		"celular": "61996320102",
		"email": "contato@tecff.com.br",
		"niver_dia": "25",
		"niver_mes": "01",
		"sexo": "M",

		"rg": "",
		"cpf": "21894342210",

		"cnpj": "",
		"inscricao_estadual": "",
		"nome_fantasia": "",

		"cep": "71925000",
		"endereco": "QUADRA 205 LT 01 SALA",
		"numero_end": "505",
		"complemento": "ED. QUARTIER CENTER",
		"bairro": "AGUAS CLARAS",
		"cidade": "BRASILIA",
		"codigo_uf": "7",

		"observacoes": "",
		"fone_nota": "61963025645",
		"codigo_natureza": "1",
		"codigo_ibge": "5300108",
		"contribuinte_icms": "1",
		"enviar_email_nfe": "1",
		"retem_csll": "S",
		"retem_csll_perc": "2",
		"retem_irrf": "S",
		"retem_irrf_perc": "3",
		"retem_pis": "S",
		"retem_pis_perc": "4",
		"retem_cofins": "S",
		"retem_cofins_perc": "5",
		"retem_iss": "S",
		"retem_iss_perc": "6",
		"retem_prev": "S",
		"retem_prev_perc": "7",
		"retem_outros": "S",

		"chave": "25A51D2D-0205-7305-D0C6-BA2FC7BD2074"
	}
}	
"
```

***Resposta de sucesso:\***

```json
{
	"atualiza_cliente": {
		"status": "0",
		"mensagem": "",
		"codigo_cliente": "100461",
		"cpf": "32299651837",
		"cnpj": "",
		"nome": "TESTE DE INCLUSAO"
	}
}
```

***Resposta de erro:\***

```json
{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Cliente solicitado para alteração não existe."
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o código do cliente"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o perfil"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o tipo da pessoa"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o cpf"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o celular"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o nome fantasia"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o cnpj"
	}
}

{
	"atualiza_cliente": {
		"status": "1",
		"mensagem": "Informe o nome do cliente"
	}
}
```

### Consultar Clientes

Esta consulta irá retornar os 30 primeiros clientes que encontrar no banco de dados, visando não pesar o tráfego de informações e ter mais performance. O usuário deverá utilizar dos filtros para encontrar o cliente desejado.

Na consulta de clientes os seguintes filtros serão aceitos e deverão estar disponíveis no APP:

- Código do Cliente

- Nome do Cliente

- CPF

- CNPJ

- Tipo Pessoa: Apresentar uma lista fixa de opções "Pessoa Física" ou "Pessoa Juridica", no momento de enviar para o serviço, deve enviar 1 para PF ou 2 para PJ

- Empresa: Utilizar o serviço listar_empresas para apresentar as empresas disponiveis 

- Perfil: Utilizar o serviço de listar_perfis para apresentar os perfis disponiveis

- UF: Utilizar o serviço listar_estados para apresentar os estados disponiveis

- Email

- Bairro

  ​

- **observação:** Os campos inteiros como o Código do Cliente, Empresa, Tipo Pessoa e Perfil, quando não informados devem ser preenchido com valor zero com aspas

  ​

  _**Requisição:**_

```json
POST /execForcaVendas.rule?sys=GFS&json="
Exemplo de chamadas com filtros:
{
	"consultar_cliente": {
		"codigo_cliente": "0",
		"codigo_empresa": "0",
		"codigo_perfil": "0",
		"codigo_uf": "0",
		"tipo_pessoa": "0",
		"nome_cliente": "",
		"email": "",
		"cpf": "",
		"cnpj": "",
		"bairro": "",      
		"chave": "25A51D2D-0205-7305-D0C6-BA2FC7BD2074"
	}
}
```

_**Resposta de sucesso:**_

```json
{
	"consultar_clientes": {
		"status": 0,
		"mensagem": "",
		"clientes": [{
			"codigo_cliente": 35660,
			"nome_cliente": " MARIA CECILIA",
			"codigo_empresa": 1,
			"nome_empresa": "PAPELARIA ABC",
			"codigo_funcionario": 0,
			"nome_funcionario": "",
			"data_cadastro": "09/08/2016",
			"cliente_desde": "08/2016",
			"usuario_cadastro": "",
			"tipo_pessoa": 1,
			"descricao_pessoa": "Pessoa Fisica",
			"codigo_perfil": 1,
			"nome_perfil": "LOJA ABC",
			"sexo": "M",
			"cpf": "51235269191",
			"rg": "",
			"niver_dia": 0,
			"niver_mes": 0,
			"cnpj": "",
			"fantasia": "",
			"insc_estadual": "",
			"endereco": "SHIS QL 26 Conjunto 8",
			"numero_end": ".",
			"complemento": "",
			"bairro": "St H I Sul",
			"cidade": "Lago Sul",
			"cep": "71665185",
			"codigo_uf": "7",
			"sigla_uf": "DF",
			"telefone": "",
			"celular": "",
			"fone_nota": 0,
			"email": "",
			"observacao": "CEP: 71665185\n",
			"codigo_natureza": 0,
			"nome_natureza": "0 - ",
			"codigo_ibge": 5300108,
			"nome_ibge": "DF - BRASILIA",
			"contribuinte_icms": "2",
			"enviar_email_nfe": 1,
			"retem_csll": "",
			"retem_csll_perc": 0,
			"retem_irrf": "",
			"retem_irrf_perc": 0,
			"retem_pis": "",
			"retem_pis_perc": 0,
			"retem_cofins": "",
			"retem_cofins_perc": 0,
			"retem_iss": "",
			"retem_iss_perc": 0,
			"retem_prev": "",
			"retem_prev_perc": 0,
			"retem_outros": ""
		}, {
			"codigo_cliente": 15369,
			"nome_cliente": " MARIA CRISTINA MARQUES DA SILVA",
			"codigo_empresa": 1,
			"nome_empresa": "PAPELARIA ABC",
			"codigo_funcionario": 0,
			"nome_funcionario": "",
			"data_cadastro": "09/08/2016",
			"cliente_desde": "08/2016",
			"usuario_cadastro": "",
			"tipo_pessoa": 1,
			"descricao_pessoa": "Pessoa Fisica",
			"codigo_perfil": 1,
			"nome_perfil": "LOJA ABC",
			"sexo": "M",
			"cpf": "72268506720",
			"rg": "",
			"niver_dia": 0,
			"niver_mes": 0,
			"cnpj": "72268506720",
			"fantasia": "",
			"insc_estadual": "",
			"endereco": "ROD DF 250 KM 2 5 ETAPA  REGIAO DOS LAGOS",
			"numero_end": ".",
			"complemento": "",
			"bairro": "SOBRADINHO",
			"cidade": "BRASILIA",
			"cep": "72255902",
			"codigo_uf": "7",
			"sigla_uf": "DF",
			"telefone": "41419014",
			"celular": "",
			"fone_nota": 0,
			"email": "",
			"observacao": "CEP: 72255902\nCHEQUE PRE DATADO   ",
			"codigo_natureza": 0,
			"nome_natureza": "0 - ",
			"codigo_ibge": 5300108,
			"nome_ibge": "DF - BRASILIA",
			"contribuinte_icms": "1",
			"enviar_email_nfe": 1,
			"retem_csll": "",
			"retem_csll_perc": 0,
			"retem_irrf": "",
			"retem_irrf_perc": 0,
			"retem_pis": "",
			"retem_pis_perc": 0,
			"retem_cofins": "",
			"retem_cofins_perc": 0,
			"retem_iss": "",
			"retem_iss_perc": 0,
			"retem_prev": "",
			"retem_prev_perc": 0,
			"retem_outros": ""
		}]
	}
}
                    
ESTE RETORNO COM STATUS 0 MAS COM A LISTA VAZIA, INDICA QUE NÃO HÁ REGISTROS                    
{
	"consultar_clientes": {
		"status": 0,
		"mensagem": "",
		"clientes": []
	}
}
```

_**Resposta de erro:**_

```json
{
	"consultar_clientes": {
		"status": 999,
		"mensagem": "Chave inválida ou inativa!"
	}
}

{
	"consultar_clientes": {
		"status": 1,
		"mensagem": "Informe o token de autorização"
	}
}

```

### Excluir Cliente

Este serviço realiza a exclusão do cliente.



**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"excluir_cliente": {
		"codigo_cliente": "",
		"chave": "F18FE4C1-F16B-FAFA-F1D8-8EE868731922"
	}
}
```

**\*Resposta de sucesso:***

```json
{
	"excluir_cliente": {
		"status": "0",
		"mensagem": "Cliente excluido com sucesso"
	}
}
```

**\*Resposta de erro:***

```json
{
    "excluir_cliente": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"excluir_cliente": {
		"status": "1",
		"mensagem": "Informe o código do cliente"
	}
}
{
	"excluir_cliente": {
		"status": "2",
		"mensagem": "Não foi possível excluir o cliente. Este cliente pode possuir relações no sistema"
	}
}
```

### Buscar Cliente

Função utilizada para buscar o cliente pelo código, cpf ou cnpj. Neste serviço os dados serão recuperados para uma possível troca de cliente na venda ou uma simples visualização dos dados do cliente.

Ao recuperar os dados do cliente no momento de realizar a alteração do cliente na venda se alguns dos valores de saldo de cashback, saldo da conta ou crédito de troca estiverem preenchidos, deverá ser apresentado para o usuário na tela esses valores, bem como o preenchimento do nome do cliente no campo devido.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"excluir_cliente": {
		"codigo_cliente": "",
		"chave": "F18FE4C1-F16B-FAFA-F1D8-8EE868731922"
	}
}
```

**\*Resposta de sucesso:***

```json
EXEMPLO DE CLIENTE COM CRÉDITO DE TROCA
{
	"buscar_cliente": {
		"status": 0,
		"mensagem": "",
		"codigo_cliente": 10001,
		"nome_cliente": "FERNANDO CARNEIRO BRASIL",
		"tipo_pessoa": 1,
		"descricao_pessoa": "Pessoa Fisica",
		"cpf": "66510147149",
		"cnpj": "",
		"endereco": "SCS QD.06 Nº 110 SL.315ED.ARNALDO VILARES",
		"numero_end": ".",
		"complemento": "",
		"bairro": "ASA SUL",
		"cidade": "BRASILIA",
		"cep": "70324900",
		"codigo_uf": 7,
		"sigla_uf": "DF",
		"telefone": "3964-7668",
		"celular": "",
		"codigo_perfil": 1,
		"nome_perfil": "LOJA ABC",
		"saldo_conta": "0,00",
		"saldo_cashback": "0,00",
		"codigo_troca": 3,
		"credito_troca": "13,90"
	}
}

EXEMPLO DE CLIENTE COM SALDO DE CASHBACK
{
	"buscar_cliente": {
		"status": 0,
		"mensagem": "",
		"codigo_cliente": 66230,
		"nome_cliente": "LILIANE MARIA ABREL PAIVA",
		"tipo_pessoa": 1,
		"descricao_pessoa": "Pessoa Fisica",
		"cpf": "32501595300",
		"cnpj": "",
		"endereco": "SHIS QI 3 CONJUNTO 9",
		"numero_end": "19",
		"complemento": "",
		"bairro": "SETOR DE HABITAÇÕES INDIVIDUAIS SUL",
		"cidade": "BRASÍLIA",
		"cep": "71605290",
		"codigo_uf": 7,
		"sigla_uf": "DF",
		"telefone": "999758092",
		"celular": "",
		"codigo_perfil": 1,
		"nome_perfil": "LOJA ABC",
		"saldo_conta": "0,00",
		"saldo_cashback": "54,01",
		"codigo_troca": 0,
		"credito_troca": "0,00"
	}
}

EXEMPLO DE CLIENTE COM SALDO DE CONTA
{
	"buscar_cliente": {
		"status": 0,
		"mensagem": "",
		"codigo_cliente": 8366,
		"nome_cliente": "AD BRASILIA MODOS LTDA",
		"tipo_pessoa": 2,
		"descricao_pessoa": "Pessoa Juridica",
		"cpf": "",
		"cnpj": "04080023000104",
		"endereco": "SDN CONJ A LOTE T51  CONJ.NACIONAL TERREO",
		"numero_end": ".",
		"complemento": "",
		"bairro": "ASA NORTE",
		"cidade": "BRASILIA",
		"cep": "70000000",
		"codigo_uf": 7,
		"sigla_uf": "DF",
		"telefone": "33279809",
		"celular": "",
		"codigo_perfil": 1,
		"nome_perfil": "LOJA ABC",
		"saldo_conta": "149,60",
		"saldo_cashback": "0,00",
		"codigo_troca": 0,
		"credito_troca": "0,00"
	}
}
```

**\*Resposta de erro:***

```json
{
    "buscar_cliente": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"buscar_cliente": {
		"status": 1,
		"mensagem": "Cliente não foi encontrado"
	}
}
```

### Alterar vendedor

Função utilizada para permitir alterar o vendedor do pedido. Neste serviço será necessário selecionar o Pedido e o novo Vendedor.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"alterar_vendedor_venda": {
		"codigo_venda": "168962",
        "codigo_funcionario": "540",
		"chave": "74CE6E90-6073-5B9C-E43B-70E3C57F0563"
	}
}
```

**\*Resposta de sucesso:***

```json
{
    "alterar_vendedor_venda":{
        "status":0,
        "mensagem":"Vendedor alterado com sucesso!"
    }
}
```

**\*Resposta de erro:***

```json
{
    "alterar_vendedor_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"alterar_vendedor_venda": {
		"status": 1,
		"mensagem": "Informe o vendedor"
	}
}
```

### Enviar venda para caixa

Função utilizada para enviar a venda para o caixa. Caso o "codigo_cliente" seja passado vazio, o serviço irá considerar como "Consumidor Final".


**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"enviar_venda_caixa": {
		"codigo_venda": "168962",
        "codigo_funcionario": "540",
        "codigo_cliente": "",
        "cpf_cnpj":"",
		"chave": "74CE6E90-6073-5B9C-E43B-70E3C57F0563"
	}
}
```

**\*Resposta de sucesso:***

```json
{
    "enviar_venda_caixa":{
        "status":0,
        "mensagem":"Venda enviada para Caixa com sucesso!"
    }
}
```

**\*Resposta de erro:***

```json
{
    "enviar_venda_caixa": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}

{
	"enviar_venda_caixa": {
		"status": 1,
		"mensagem": "Venda sem itens"
	}
}

{
	"enviar_venda_caixa": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa"
	}
}
```



### Listar Formas de Pagamento

Função utilizada para obter lista de formas de pagamentos disponíveis


**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_forma_pagamento": {
		"chave": "74CE6E90-6073-5B9C-E43B-70E3C57F0563"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "listar_forma_pagamento":{  
      "status":0,
      "mensagem":"",
      "form_pagamento":[  
         {  
            "codigo_documento":12,
            "nome_documento":"Requisição"
         },
         {  
            "codigo_documento":13,
            "nome_documento":"Dinheiro"
         },
         {  
            "codigo_documento":160,
            "nome_documento":"ELO DEBITO"
         },
         {  
            "codigo_documento":9,
            "nome_documento":"Cartão Visa - Débito"
         },
         {  
            "codigo_documento":6,
            "nome_documento":"Cartão Master - Crédito"
         },
         {  
            "codigo_documento":18,
            "nome_documento":"DEPÓSITO BANCÁRIO"
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "listar_forma_pagamento": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
```



### Gravar pagamento

Função utilizada para gravar forma de pagamento para a venda.  Caso o "valor_pagamento" não seja enviado, o serviço irá considerar o valor total a pagar.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"gravar_pagamento": {
		"codigo_venda": "168960",
        "codigo_documento": "13",
        "valor_pagamento": "2.200,00",
        "quantidade_parcela":"1",
        "codigo_autorizacao": "101213",
		"chave": "74CE6E90-6073-5B9C-E43B-70E3C57F0563"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "gravar_pagamento":{  
      "status":0,
      "mensagem":"Forma de pagamento inserida com sucesso!",
      "total_a_pagar":"2.306,82",
      "total_resta_a_pagar":"0,00",
      "total_pago":"2.306,82",
      "troco":"3,18",
      "pagamento":[  
         {  
            "codigo_pagamento":162833,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"1/3",
            "data_vencimento":"12/10/2018",
            "valor_parcela":"33,34"
         },
         {  
            "codigo_pagamento":162834,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"2/3",
            "data_vencimento":"11/11/2018",
            "valor_parcela":"33,33"
         },
         {  
            "codigo_pagamento":162835,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"3/3",
            "data_vencimento":"11/12/2018",
            "valor_parcela":"33,33"
         },
         {  
            "codigo_pagamento":162836,
            "codigo_venda":168960,
            "codigo_documento":13,
            "nome_documento":"Dinheiro",
            "codigo_autorizacao":"101213",
            "numero_documento":"1/1",
            "data_vencimento":"13/09/2018",
            "valor_parcela":"2.206,82"
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "gravar_pagamento": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
CASO A FORMA DE PAGAMENTO SEJA DIFERENTE DE DINHEIRO E O VALOR INFORMADO SEJA MAIOR QUE O VALOR RESTA A PAGAR
{  
   "gravar_pagamento":{  
      "status"  1,
      "mensagem" : "Valor informado superior ao valor que resta a pagar: 3,90"
   }
}
```



### Excluir pagamento

Função utilizada para realizar a exclusão do registro de pagamento de uma venda. O elemento "codigo_pagamento" é opcional. Para excluir todos os registros de pagamentos basta enviar o elemento vazio/nulo. Será retornada a lista de pagamentos da venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"excluir_pagamento": {
		"codigo_venda": "168960",
        "codigo_pagamento": "162837",
		"chave": "74CE6E90-6073-5B9C-E43B-70E3C57F0563"
	}
}
```

**\*Resposta de sucesso:***

```json
EXEMPLO COM EXCLUSÃO DE TODOS OS REGISTROS DE PAGAMENTO DA VENDA
{  
   "excluir_pagamento":{  
      "status":0,
      "mensagem":"Pagamento excluído com sucesso!",
      "total_a_pagar":"2.306,82",
      "total_resta_a_pagar":"2.306,82",
      "total_pago":"0,00",
      "troco":"0,00",       
      "pagamento":[]
   }
}

EXEMPLO COM EXCLUSÃO DE APENAS 1 REGISTRO DE PAGAMENTO DA VENDA
{  
   "excluir_pagamento":{  
      "status":0,
      "mensagem":"Pagamento excluído com sucesso!",
      "total_a_pagar":"2.306,82",
      "total_resta_a_pagar":"2.206,82",
      "total_pago":"100,00",
      "troco":"0,00",
      "pagamento":[  
         {  
            "codigo_pagamento":162838,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"1/4",
            "data_vencimento":"12/10/2018",
            "valor_parcela":"25,00"
         },
         {  
            "codigo_pagamento":162839,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"2/4",
            "data_vencimento":"11/11/2018",
            "valor_parcela":"25,00"
         },
         {  
            "codigo_pagamento":162840,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"3/4",
            "data_vencimento":"11/12/2018",
            "valor_parcela":"25,00"
         },
         {  
            "codigo_pagamento":162841,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"4/4",
            "data_vencimento":"10/01/2019",
            "valor_parcela":"25,00"
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "excluir_pagamento": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"excluir_pagamento": {
		"status": 1,
		"mensagem": "A Venda já foi fechada. Não é possível excluir o pagamento."
	}
}
```



### Alterar pagamento

Função utilizada para realizar a alteração do registro de pagamento de uma venda. Será retornada a lista de pagamentos da venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"alterar_pagamento": {
		"codigo_venda": "168960",
        "codigo_pagamento": "162837",
		"codigo_documento": "13",    
        "data_vencimento": "12/09/2018",         
        "numero_documento": "dinheiro",
        "codigo_autorizacao": "",       
		"chave": "9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "alterar_pagamento":{  
      "status":0,
      "mensagem":"Pagamento alterado com sucesso!",
      "total_a_pagar":"2.306,82",
      "total_resta_a_pagar":"0,00",
      "total_pago":"2.306,82",
      "troco":"0,00",
      "pagamento":[  
         {  
            "codigo_pagamento":162837,
            "codigo_venda":168960,
            "codigo_documento":13,
            "nome_documento":"Dinheiro",
            "codigo_autorizacao":"",
            "numero_documento":"dinheiro",
            "data_vencimento":"12/09/2018",
            "valor_parcela":"2.206,82"
         },
         {  
            "codigo_pagamento":162838,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"1/4",
            "data_vencimento":"12/10/2018",
            "valor_parcela":"25,00"
         },
         {  
            "codigo_pagamento":162839,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"2/4",
            "data_vencimento":"11/11/2018",
            "valor_parcela":"25,00"
         },
         {  
            "codigo_pagamento":162840,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"3/4",
            "data_vencimento":"11/12/2018",
            "valor_parcela":"25,00"
         },
         {  
            "codigo_pagamento":162841,
            "codigo_venda":168960,
            "codigo_documento":8,
            "nome_documento":"Cartão Visa - Crédito",
            "codigo_autorizacao":"101213",
            "numero_documento":"4/4",
            "data_vencimento":"10/01/2019",
            "valor_parcela":"25,00"
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "alterar_pagamento": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"alterar_pagamento": {
		"status": 1,
		"mensagem": "Forma de pagamento não informada"
	}
}
```



### Listar pagamentos

Função utilizada para apresentar lista de pagamentos da venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_pagamento": {
		"codigo_venda":"168960",      
		"chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{"listar_pagamento":{  
   "status":0,
   "mensagem":"Consulta realizada com sucesso!",
   "total_a_pagar":"2.306,82",
   "total_resta_a_pagar":"0,00",
   "total_pago":"2.306,82",
   "troco":"0,00",
   "pagamento":[  
      {  
         "codigo_pagamento":162837,
         "codigo_venda":168960,
         "codigo_documento":13,
         "nome_documento":"Dinheiro",
         "codigo_autorizacao":"101213",
         "numero_documento":"1/1",
         "data_vencimento":"13/09/2018",
         "valor_parcela":"2.206,82"
      },
      {  
         "codigo_pagamento":162838,
         "codigo_venda":168960,
         "codigo_documento":8,
         "nome_documento":"Cartão Visa - Crédito",
         "codigo_autorizacao":"101213",
         "numero_documento":"1/4",
         "data_vencimento":"12/10/2018",
         "valor_parcela":"25,00"
      },
      {  
         "codigo_pagamento":162839,
         "codigo_venda":168960,
         "codigo_documento":8,
         "nome_documento":"Cartão Visa - Crédito",
         "codigo_autorizacao":"101213",
         "numero_documento":"2/4",
         "data_vencimento":"11/11/2018",
         "valor_parcela":"25,00"
      },
      {  
         "codigo_pagamento":162840,
         "codigo_venda":168960,
         "codigo_documento":8,
         "nome_documento":"Cartão Visa - Crédito",
         "codigo_autorizacao":"101213",
         "numero_documento":"3/4",
         "data_vencimento":"11/12/2018",
         "valor_parcela":"25,00"
      },
      {  
         "codigo_pagamento":162841,
         "codigo_venda":168960,
         "codigo_documento":8,
         "nome_documento":"Cartão Visa - Crédito",
         "codigo_autorizacao":"101213",
         "numero_documento":"4/4",
         "data_vencimento":"10/01/2019",
         "valor_parcela":"25,00"
      }
   ]
}
}
```

**\*Resposta de erro:***

```json
{
    "listar_pagamento": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
```

### 



### Listar Grupos de Lista de Materiais

Função utilizada para apresentar lista de grupos de listas de materiais.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_grupo_lista": {
		"codigo_lista":"2123",      
		"chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{"listar_grupo_lista":{  
   "status":0,
   "mensagem":"Consulta realizada com sucesso!",
   "grupo_lista":[  
      {  
         "codigo_lista":2123,
         "codigo_grupo_lista":9,
         "nome_grupo_lista":"Artes"
      },
      {  
         "codigo_lista":2123,
         "codigo_grupo_lista":1,
         "nome_grupo_lista":"Individual"
      },
      {  
         "codigo_lista":2123,
         "codigo_grupo_lista":3,
         "nome_grupo_lista":"Livros"
      }
   ]
}
}
```

**\*Resposta de erro:***

```json
{
    "listar_grupo_lista": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"listar_grupo_lista": {
		"status": 1,
		"mensagem": "Lista não informada"
	}
}
```

### 

### Carregar lista

Função utilizada para carregar lista de produtos escolares.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"carregar_lista": {
		"codigo_venda":"168960",      
		"codigo_lista":"2123",    
		"codigo_grupo_lista":"1",            
		"codigo_empresa":"1",    
		"codigo_funcionario":"160",  
        "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "carregar_lista":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"1.888,91",
      "total_resta_a_pagar":"1.788,91",
      "total_pago":"100,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168960,
         "quantidade_total":"63",
         "subtotal":"1.889,44",
         "total_desconto":"0,53",
         "total_acrescimos":"0,00",
         "total_final":"1.888,91",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },         
      "itens_venda":[  
         {  
            "codigo_item_venda":1158470,
            "codigo_produto":741566,
            "codigo_personalizado":"",
            "codigo_barras":"7894494081361",
            "codigo_apresentacao":"741566",
            "nome_produto":"CAD JANDAIA BRASILIDADE CD UNIV 01 MAT 96 FLS 8136",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"5,99",
            "valor_desconto":"0,00",
            "total_produto":"17,97",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158469,
            "codigo_produto":4053257,
            "codigo_personalizado":"",
            "codigo_barras":"7894494625053",
            "codigo_apresentacao":"4053257",
            "nome_produto":"CADERNETA JANDAIA ANOTACOES DUO 95X140 80FLS 62505",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"22,99",
            "valor_desconto":"0,00",
            "total_produto":"22,99",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158468,
            "codigo_produto":58700,
            "codigo_personalizado":"",
            "codigo_barras":"",
            "codigo_apresentacao":"58700",
            "nome_produto":"CANETA ESF CRISTAL BIC AZ",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"1,25",
            "valor_desconto":"0,00",
            "total_produto":"3,75",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158467,
            "codigo_produto":4063520,
            "codigo_personalizado":"",
            "codigo_barras":"3154148505211",
            "codigo_apresentacao":"4063520",
            "nome_produto":"LAPIS GRAFITE MAPED ESSENTIALS HB2 850521",
            "sigla_unidade":"UND",
            "quantidade_itens":"3",
            "valor_venda":"0,80",
            "valor_desconto":"0,00",
            "total_produto":"2,40",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158466,
            "codigo_produto":37796,
            "codigo_personalizado":"",
            "codigo_barras":"7896326987780",
            "codigo_apresentacao":"37796",
            "nome_produto":"BORRACHA CIS PLAST BR",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"1,60",
            "valor_desconto":"0,00",
            "total_produto":"1,60",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158465,
            "codigo_produto":917842,
            "codigo_personalizado":"",
            "codigo_barras":"7896326951293",
            "codigo_apresentacao":"917842",
            "nome_produto":"APONTADOR ESC CIS PLAST DEP 310",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"1,99",
            "valor_desconto":"0,00",
            "total_produto":"1,99",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "carregar_lista": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"carregar_lista": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa"
	}
}
```

### 

### Listar item venda

Função utilizada para carregar lista de itens da venda. Permite retornar um item da venda ou todos os itens da venda. Para listar todos os itens da venda é necessário enviar o elemento "codigo_item_venda" com o valor 0 (zero).

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"listar_item_venda": {
		"codigo_venda":"168960",      
		"codigo_item_venda":"0",    
		"nome_elemento_principal":"",            
		"mensagem":""
	}
}
```

**\*Resposta de sucesso:***

```json
EXEMPLO SEM INFORMAR O NOME DO ELEMENTO PRINCIPAL
{  
   "listar_item_venda":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"1.888,91",
      "total_resta_a_pagar":"1.788,91",
      "total_pago":"100,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168960,
         "quantidade_total":"63",
         "subtotal":"1.889,44",
         "total_desconto":"0,53",
         "total_acrescimos":"0,00",
         "total_final":"1.888,91",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },       
      "itens_venda":[  
         {  
            "codigo_item_venda":1158470,
            "codigo_produto":741566,
            "codigo_personalizado":"",
            "codigo_barras":"7894494081361",
            "codigo_apresentacao":"741566",
            "nome_produto":"CAD JANDAIA BRASILIDADE CD UNIV 01 MAT 96 FLS 8136",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"5,99",
            "valor_desconto":"0,00",
            "total_produto":"17,97",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158469,
            "codigo_produto":4053257,
            "codigo_personalizado":"",
            "codigo_barras":"7894494625053",
            "codigo_apresentacao":"4053257",
            "nome_produto":"CADERNETA JANDAIA ANOTACOES DUO 95X140 80FLS 62505",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"22,99",
            "valor_desconto":"0,00",
            "total_produto":"22,99",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158468,
            "codigo_produto":58700,
            "codigo_personalizado":"",
            "codigo_barras":"",
            "codigo_apresentacao":"58700",
            "nome_produto":"CANETA ESF CRISTAL BIC AZ",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"1,25",
            "valor_desconto":"0,00",
            "total_produto":"3,75",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         }
      ]
   }
}

EXEMPLO INFORMANDO O NOME DO ELEMENTO PRINCIPAL
{  
   "nome_do_elemento":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"1.888,91",
      "total_resta_a_pagar":"1.788,91",
      "total_pago":"100,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168960,
         "quantidade_total":"63",
         "subtotal":"1.889,44",
         "total_desconto":"0,53",
         "total_acrescimos":"0,00",
         "total_final":"1.888,91",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },    
      "itens_venda":[  
         {  
            "codigo_item_venda":1158470,
            "codigo_produto":741566,
            "codigo_personalizado":"",
            "codigo_barras":"7894494081361",
            "codigo_apresentacao":"741566",
            "nome_produto":"CAD JANDAIA BRASILIDADE CD UNIV 01 MAT 96 FLS 8136",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"5,99",
            "valor_desconto":"0,00",
            "total_produto":"17,97",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158469,
            "codigo_produto":4053257,
            "codigo_personalizado":"",
            "codigo_barras":"7894494625053",
            "codigo_apresentacao":"4053257",
            "nome_produto":"CADERNETA JANDAIA ANOTACOES DUO 95X140 80FLS 62505",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"22,99",
            "valor_desconto":"0,00",
            "total_produto":"22,99",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158468,
            "codigo_produto":58700,
            "codigo_personalizado":"",
            "codigo_barras":"",
            "codigo_apresentacao":"58700",
            "nome_produto":"CANETA ESF CRISTAL BIC AZ",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"1,25",
            "valor_desconto":"0,00",
            "total_produto":"3,75",
            "data_hora_cadastro":"11/09/2018 14:01",
            "hora_cadastro":"14:01",
            "vendedor_item":"SUPORTE",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
Sem retorno
```

### 

### Alterar quantidade do item da venda

Função utilizada para permitir alterar a quantidade de itens da venda através do atalho de soma e subtração. Função 0 - Subtrai / 1 - Soma.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"alterar_qtd_item_venda": {
		"codigo_venda":"168960",      
		"codigo_item_venda":"1158529",    
		"funcao":"1",            
        "codigo_funcionario":"160",  
        "chave": "9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "alterar_qtd_item_venda":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"1.887,21",
      "total_resta_a_pagar":"1.787,21",
      "total_pago":"100,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168960,
         "quantidade_total":"62",
         "subtotal":"1.887,45",
         "total_desconto":"0,24",
         "total_acrescimos":"0,00",
         "total_final":"1.887,21",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },
      "itens_venda":[  
         {  
            "codigo_item_venda":1158529,
            "codigo_produto":917842,
            "codigo_personalizado":"",
            "codigo_barras":"7896326951293",
            "codigo_apresentacao":"917842",
            "nome_produto":"APONTADOR ESC CIS PLAST DEP 310",
            "sigla_unidade":"UN",
            "quantidade_itens":"2",
            "valor_venda":"1,99",
            "valor_desconto":"0,00",
            "total_produto":"3,98",
            "data_hora_cadastro":"12/09/2018 13:49",
            "hora_cadastro":"13:49",
            "vendedor_item":"SUPORTE",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "alterar_qtd_item_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}

{
	"alterar_qtd_item_venda": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa"
	}
}

{  
   "alterar_qtd_item_venda":{  
      "status":1,
      "mensagem":"Não é possível subtrair deste lançamento."
   }
}
```

### 

### Alterar item da venda

Função utilizada para permitir alterar a quantidade e/ou desconto de itens da venda. O desconto pode ser alterado usando o elemento "valor_desconto" ou "percent_desconto". A prioridade será dada ao elemento "valor_desconto". Ou seja, o serviço verifica se o elemento "valor_desconto" é diferente de 0 (zero), se não valida o elemento "percent_desconto". Se ambos os elementos forem iguais a 0 (zero), o valor do desconto será zerado para o item da venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"alterar_item_venda": {
		"codigo_venda":"169064",      
		"codigo_item_venda":"1157592",
        "quantidade_itens":"3,00",
		"valor_desconto":"0",            
		"percent_desconto":"0",            
        "codigo_funcionario":"160",  
        "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "alterar_item_venda":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"1.888,91",
      "total_resta_a_pagar":"1.788,91",
      "total_pago":"100,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168960,
         "quantidade_total":"63",
         "subtotal":"1.889,44",
         "total_desconto":"0,53",
         "total_acrescimos":"0,00",
         "total_final":"1.888,91",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },
      "itens_venda":[  
         {  
            "codigo_item_venda":1158529,
            "codigo_produto":917842,
            "codigo_personalizado":"",
            "codigo_barras":"7896326951293",
            "codigo_apresentacao":"917842",
            "nome_produto":"APONTADOR ESC CIS PLAST DEP 310",
            "sigla_unidade":"UN",
            "quantidade_itens":"3",
            "valor_venda":"1,99",
            "valor_desconto":"0,29",
            "total_produto":"5,68",
            "data_hora_cadastro":"12/09/2018 13:49",
            "hora_cadastro":"13:49",
            "vendedor_item":"SUPORTE",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "alterar_item_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}

{
	"alterar_item_venda": {
		"status": 1,
		"mensagem":"O pedido já foi enviado para o caixa!"
	}
}

{  
   "alterar_item_venda":{  
      "status":1,
      "mensagem":"Produto em promoção não permite desconto!"
   }
}
```

### 

### Excluir item da venda

Função utilizada para permitir excluir um ou todos os itens da venda. Para excluir todos os itens da venda é necessário enviar o elemento "codigo_item_venda" com o valor 0 (zero). O serviço irá retornar a lista de itens da venda e atualizará os valores da venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"excluir_item_venda": {
		"codigo_venda": "168960",      
		"codigo_item_venda": "1158579",    
        "codigo_funcionario": "160",  
        "chave": "9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
 "excluir_item_venda":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"1.888,91",
      "total_resta_a_pagar":"1.788,91",
      "total_pago":"100,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168960,
         "quantidade_total":"63",
         "subtotal":"1.889,44",
         "total_desconto":"0,53",
         "total_acrescimos":"0,00",
         "total_final":"1.888,91",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },
      "itens_venda":[  
         {  
            "codigo_item_venda":1158578,
            "codigo_produto":4081616,
            "codigo_personalizado":"",
            "codigo_barras":"",
            "codigo_apresentacao":"4081616",
            "nome_produto":"GRAMATICA   TEXTO   REFLEXAO E USOATUAL",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"199,00",
            "valor_desconto":"0,00",
            "total_produto":"199,00",
            "data_hora_cadastro":"12/09/2018 13:49",
            "hora_cadastro":"13:49",
            "vendedor_item":"SUPORTE",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158577,
            "codigo_produto":929719,
            "codigo_personalizado":"",
            "codigo_barras":"9788508172399",
            "codigo_apresentacao":"929719",
            "nome_produto":"PROJETO TELARIS PORTUGUES 7 ANO ATICA",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"182,00",
            "valor_desconto":"0,00",
            "total_produto":"182,00",
            "data_hora_cadastro":"12/09/2018 13:49",
            "hora_cadastro":"13:49",
            "vendedor_item":"SUPORTE",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "excluir_item_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}

{
	"excluir_item_venda": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa"
	}
}

{  
   "excluir_item_venda":{  
      "status":1,
      "mensagem":"Vendedor não informado."
   }
}
```

### 

### Consultar vale livro

Função utilizada para listar Vale livros com os detalhes. A consulta pode ser realizada por "codigo_venda", "codigo_vale", "codigo_cliente" ou "codigo_empresa". É necessário informar ao menos 1 dos elementos para executar a consulta. A consulta irá retornar até 30 registros, ordenados de forma descendente.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"consultar_vale": {
		"codigo_venda": "0",      
		"codigo_vale": "0",    
        "codigo_empresa": "3",
        "codigo_cliente": "0",        
        "chave": "9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "consultar_vale":{  
      "status":0,
      "mensagem":"",
      "vale":[  
         {  
            "codigo_vale":3205,
            "codigo_venda":160195,
            "data_prevista":"11/03/2018",
            "nome_cliente":"SUELEN ABREU PEDRO",
            "endereco":"AOS 4 BLOCO D APT 501",
            "bairro":"",
            "cidade":"",
            "cep":"70660044",
            "telefone":"- 993331184",
            "celular":"",
            "observacao":"Acesse o vale livro pelo endereço  http://valelivro.abcloja.com.br:9004/vale",
            "status":"Pendente",
            "data_cadastro":"09/02/2018",
            "hora_cadastro":"11:52",
            "data_pagamento":"09/02/2018",
            "hora_pagamento":"12:12",
            "email":"suelenabreu@gmail.com",
            "quantidade_itens":"1,00",
            "valor_total":"153,80",
            "aluno_vale":[  
               {  
                  "codigo_aluno":3489,
                  "nome_aluno":"SUELEN ABREU PEDRO",
                  "nome_escola":"CASA DA CRIANÇA",
                  "nome_serie":"1 PERIODO",
                  "nome_turno":"MATUTINO",
                  "item_aluno_vale":[  
                     {  
                        "codigo_item_vale":38911,
                        "codigo_produto":183326,
                        "nome_produto":"PROJETO ECO MIRIM GRUPO 04 - ED.POSITIV0",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"153,80",
                        "total_produto":"153,80",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     }
                  ]
               }
            ]
         },
         {  
            "codigo_vale":3059,
            "codigo_venda":151748,
            "data_prevista":"23/02/2018",
            "nome_cliente":"STARK CONSTRUÇOES LTDA ME",
            "endereco":"RUA 34 NORTE LT 4 LJ 4   ED REAL FLAT",
            "bairro":"",
            "cidade":"",
            "cep":"71918720",
            "telefone":"- 3209-3998 -",
            "celular":"",
            "observacao":"Acesse o vale livro pelo endereço  http://valelivro.abcloja.com.br:9004/vale",
            "status":"Pendente",
            "data_cadastro":"24/01/2018",
            "hora_cadastro":"17:00",
            "data_pagamento":"25/01/2018",
            "hora_pagamento":"09:22",
            "email":"contato@starkcontrucoes.com.br",
            "quantidade_itens":"4,00",
            "valor_total":"632,00",
            "aluno_vale":[  
               {  
                  "codigo_aluno":3327,
                  "nome_aluno":"RANGEL CARLOS DE MATOS",
                  "nome_escola":"ABC EDUCACAO TESTE",
                  "nome_serie":"MATERNAL BABY",
                  "nome_turno":"MATUTINO",
                  "item_aluno_vale":[  
                     {  
                        "codigo_item_vale":37689,
                        "codigo_produto":4077648,
                        "nome_produto":"CHALLENGE\nMODERNA",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"150,00",
                        "total_produto":"150,00",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     },
                     {  
                        "codigo_item_vale":37690,
                        "codigo_produto":4011163,
                        "nome_produto":"MODERNA PLUS FILOSOFANDOMODERNA",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"225,00",
                        "total_produto":"225,00",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     },
                     {  
                        "codigo_item_vale":37691,
                        "codigo_produto":956287,
                        "nome_produto":"CAMINOS ESPANOL LEGUA Y CULTURA 7ANO",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"112,00",
                        "total_produto":"112,00",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     },
                     {  
                        "codigo_item_vale":37692,
                        "codigo_produto":4079824,
                        "nome_produto":"SOCIOLOGIA HOJEATICA",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"145,00",
                        "total_produto":"145,00",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "consultar_vale": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}

{
	"consultar_vale": {
		"status": 1,
		"mensagem": "É necessário informar ao menos 1 filtro!"
	}
}

```

### 

### Gerar Vale Livro

Função utilizada para Gerar Vale Livro a partir de uma Pré Venda. O Vale pode ser gerado a partir da lista de selecionados "selecionados" ou todos os livros da venda. O servilço retorna a consulta do vale livro em caso de sucesso.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
EXEMPLO COM LISTA DE SELECIONADOS
{
	"gerar_vale_livro": {
		"codigo_venda":"168963",      
		"codigo_funcionario":"160", 
        "codigo_cliente":"1",    
      	"codigo_empresa":"1",    
       	"selecionados":"1158580, 1158581",    
        "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}

EXEMPLO PARA INSERIR TODOS OS LIVROS DA VENDA
{
	"gerar_vale_livro": {
		"codigo_venda":"168963",      
		"codigo_funcionario":"160", 
        "codigo_cliente":"1",    
      	"codigo_empresa":"1",    
       	"selecionados":"",    
        "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "consultar_vale":{  
      "status":0,
      "mensagem":"",
      "vale":[  
         {  
            "codigo_vale":3248,
            "codigo_venda":168963,
            "data_prevista":"22/10/2018",
            "nome_cliente":"CLUBE DO CONGRESSO",
            "endereco":"SEPS 702/902 BLOCO C",
            "bairro":"",
            "cidade":"",
            "cep":"70330035",
            "telefone":"33254944",
            "celular":"",
            "observacao":"Acesse o vale livro pelo endereço  http://valelivro.abcloja.com.br:9004/vale",
            "status":"Pago",
            "data_cadastro":"22/09/2018",
            "hora_cadastro":"11:20",
            "data_pagamento":"01/01/0001",
            "hora_pagamento":"00:00",
            "email":"",
            "quantidade_itens":"0,00",
            "valor_total":"0,00",
            "aluno_vale":[  
               {  
                  "codigo_aluno":3532,
                  "nome_aluno":"PAPELARIA ABC",
                  "nome_escola":"CIMAN",
                  "nome_serie":"MATERNAL BABY",
                  "nome_turno":"MATUTINO",
                  "item_aluno_vale":[  
                     {  
                        "codigo_item_vale":39042,
                        "codigo_produto":231550,
                        "nome_produto":"ALMOFADA CARIMBO RADEX Nº 3 PT",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"3,90",
                        "total_produto":"3,90",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     },
                     {  
                        "codigo_item_vale":39043,
                        "codigo_produto":77682,
                        "nome_produto":"EXPERIMENTANDO A BIOLOGIA ED.ENOVUS VOL.01",
                        "quantidade_itens":"1,00",
                        "quantidade_recebida":"0,00",
                        "valor_venda":"90,00",
                        "total_produto":"90,00",
                        "data_pedido":"01/01/0001",
                        "encapar":"N",
                        "etiquetar":"N",
                        "separado":"N",
                        "data_separacao":"01/01/0001",
                        "hora_separacao":"00:00",
                        "entregue":"N",
                        "data_entrega":"01/01/0001",
                        "hora_entrega":"00:00",
                        "situacao_entrada_vale":"",
                        "observacao":""
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "gerar_vale_livro": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"gerar_vale_livro": {
		"status": 1,
		"mensagem": "Não é possível Gerar vale livro para cliente consumidor final"
	}
}
{
	"gerar_vale_livro": {
		"status": 1,
		"mensagem": "Venda sem itens lançados"
	}
}
{
	"gerar_vale_livro": {
		"status": 1,
		"mensagem": "Selecione os itens que deseja adicionar no vale"
	}
}
```

### 

### Gravar venda

Função utilizada para gravar a venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"gravar_venda": {
		"codigo_venda":"168963",      
		"codigo_funcionario":"160", 
        "codigo_cliente":"1",    
      	"cpf_cnpj":"",    
        "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{
   "gravar_venda":{
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"116,89",
      "total_resta_a_pagar":"116,89",
      "total_pago":"0,00",
      "troco":"0,00",
      "totaliza_venda":{
         "status":0,
         "mensagem":"",
         "codigo_venda":168963,
         "quantidade_total":"3",
         "subtotal":"116,89",
         "total_desconto":"0,00",
         "total_acrescimos":"0,00",
         "total_final":"116,89",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },
      "itens_venda":[
         {
            "codigo_item_venda":1158582,
            "codigo_produto":1309,
            "codigo_personalizado":"",
            "codigo_barras":"7896572002077",
            "codigo_apresentacao":"1309",
            "nome_produto":"ABC COMPACTOR 75MM",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"22,99",
            "valor_desconto":"0,00",
            "total_produto":"22,99",
            "data_hora_cadastro":"21/09/2018 16:27",
            "hora_cadastro":"16:27",
            "vendedor_item":"VINICIUS",
            "observacao":""
         },
         {
            "codigo_item_venda":1158581,
            "codigo_produto":77682,
            "codigo_personalizado":"",
            "codigo_barras":"9788566563030",
            "codigo_apresentacao":"77682",
            "nome_produto":"EXPERIMENTANDO A BIOLOGIA ED.ENOVUS VOL.01",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"90,00",
            "valor_desconto":"0,00",
            "total_produto":"90,00",
            "data_hora_cadastro":"21/09/2018 16:27",
            "hora_cadastro":"16:27",
            "vendedor_item":"VINICIUS",
            "observacao":""
         },
         {
            "codigo_item_venda":1158580,
            "codigo_produto":231550,
            "codigo_personalizado":"",
            "codigo_barras":"7897254101309",
            "codigo_apresentacao":"231550",
            "nome_produto":"ALMOFADA CARIMBO RADEX Nº 3 PT",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"3,90",
            "valor_desconto":"0,00",
            "total_produto":"3,90",
            "data_hora_cadastro":"21/09/2018 16:27",
            "hora_cadastro":"16:27",
            "vendedor_item":"VINICIUS",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "gravar_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"gravar_venda": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa"
	}
}
{
	"gravar_venda": {
		"status": 1,
		"mensagem": "Venda sem itens lançados"
	}
}

```

### 

### Aplicar desconto na venda

Função utilizada para executar desconto nos produtos da venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"aplicar_desconto_venda": {
		"codigo_venda":"169064",      
		"codigo_funcionario":"160",
         "senha":"1515",
		"valor_desconto":"0",            
		"percent_desconto":"0",            
         "valor_total":"111,00",  
         "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "aplicar_desconto_venda":{  
      "status":0,
      "mensagem":"Sucesso",
      "total_a_pagar":"111,00",
      "total_resta_a_pagar":"111,00",
      "total_pago":"0,00",
      "troco":"0,00",
      "totaliza_venda":{  
         "status":0,
         "mensagem":"",
         "codigo_venda":168963,
         "quantidade_total":"3",
         "subtotal":"116,89",
         "total_desconto":"5,89",
         "total_acrescimos":"0,00",
         "total_final":"111,00",
         "total_cashback":"0,00",
         "total_servico":"0,00",
         "total_entrega":"0,00"
      },
      "itens_venda":[  
         {  
            "codigo_item_venda":1158582,
            "codigo_produto":1309,
            "codigo_personalizado":"",
            "codigo_barras":"7896572002077",
            "codigo_apresentacao":"1309",
            "nome_produto":"ABC COMPACTOR 75MM",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"22,99",
            "valor_desconto":"0,00",
            "total_produto":"22,99",
            "data_hora_cadastro":"21/09/2018 16:27",
            "hora_cadastro":"16:27",
            "vendedor_item":"VINICIUS",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158581,
            "codigo_produto":77682,
            "codigo_personalizado":"",
            "codigo_barras":"9788566563030",
            "codigo_apresentacao":"77682",
            "nome_produto":"EXPERIMENTANDO A BIOLOGIA ED.ENOVUS VOL.01",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"90,00",
            "valor_desconto":"5,65",
            "total_produto":"84,35",
            "data_hora_cadastro":"21/09/2018 16:27",
            "hora_cadastro":"16:27",
            "vendedor_item":"VINICIUS",
            "observacao":""
         },
         {  
            "codigo_item_venda":1158580,
            "codigo_produto":231550,
            "codigo_personalizado":"",
            "codigo_barras":"7897254101309",
            "codigo_apresentacao":"231550",
            "nome_produto":"ALMOFADA CARIMBO RADEX Nº 3 PT",
            "sigla_unidade":"UN",
            "quantidade_itens":"1",
            "valor_venda":"3,90",
            "valor_desconto":"0,24",
            "total_produto":"3,66",
            "data_hora_cadastro":"21/09/2018 16:27",
            "hora_cadastro":"16:27",
            "vendedor_item":"VINICIUS",
            "observacao":""
         }
      ]
   }
}
```

**\*Resposta de erro:***

```json
{
    "aplicar_desconto_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"aplicar_desconto_venda": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa."
	}
}
{
	"aplicar_desconto_venda": {
		"status": 1,
		"mensagem": "Desconto maior que o permitido."
	}
}

```

### 

### Trocar Cliente da Venda

Função utilizada para executar a troca do consumidor na venda.

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{
	"trocar_cliente_venda": {
		"codigo_venda":"168963",      
		"codigo_cliente":"",
         "cpf_cnpj":"86338285100",
		"nome_cliente":"",              
         "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
	}
}
```

**\*Resposta de sucesso:***

```json
{  
   "trocar_cliente_venda":{  
      "status":0,
      "mensagem":"Consumidor alterado com sucesso",
      "codigo_cliente":"63957",
      "cpf_cnpj":"86338285100",
      "nome_cliente":"EVANDO BARBOSA TORRES",
      "mensagem_cashback":"Este cliente possui saldo de Cashback no valor de R$ 4,18",
      "valor_total_cashback":"4,18",
      "mensagem_credito":"",
      "valor_total_credito":"0,00",
      "mensagem_credito_troca":"",
      "valor_total_credito_troca":"0,00"
   }
}
```

**\*Resposta de erro:***

```json
{
    "trocar_cliente_venda": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{
	"trocar_cliente_venda": {
		"status": 1,
		"mensagem": "O pedido já foi enviado para o caixa."
	}
}
{
	"trocar_cliente_venda": {
		"status": 1,
		"mensagem": "Cliente bloqueado."
	}
}

```

### 

### Enviar e-mail

Função utilizada para executar o envio de vendas, vale livros ou lista de produtos

**\*Requisição:***

```json
POST /execForcaVendas.rule?sys=GFS&json="
{  
   "enviar_email_pedido":{  
      "codigo_venda":"",
      "codigo_vale":"",
      "codigo_lista":"2123",
      "email":"juliocesarbsi@gmail.com",
      "codigo_empresa":"3",
      "chave":"9CFE4FFB-2190-DF80-8612-A236D02E9A3F"
   }
}
```

**\*Resposta de sucesso:***

```json
{  
   "enviar_email_pedido":{  
      "status":"0",
      "mensagem":"E-mail enviado com sucesso!"
   }
}
```

**\*Resposta de erro:***

```json
{
    "enviar_email_pedido": {
        "status": 999,
        "mensagem": "Chave inválida ou inativa!"
    }
}
{  
   "enviar_email_pedido":{  
      "status":"1",
      "mensagem":"O e-mail informado (juliocesarbsi@gmail.co135m) não é válido."
   }
}
{
	"enviar_email_pedido": {
		"status": 1,
		"mensagem": "Servidor de E-mail não configurado."
	}
}

```

### 