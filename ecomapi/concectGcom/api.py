# coding=utf-8

url = 'http://201.86.129.99:9009/gwservicos/execForcaVendas.rule?sys=GFS&json='
key = 'B5850213-D758-F2D5-3A4B-3BFAFC1BC284'

jsonGera = '{%22gerarChave%22:{%22aplicacao%22:%226E8E69A8-15ED-44A9-B378-570A8298F776%22,%22chave%22:%22beb6b72231daafe7d913baa818a63f0c%22}}'
jsonEstados = '{%22listar_estados%22:{%22chave%22: %22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'
jsonEscolas = '{%22listar_escolas%22: {%22chave%22: %22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'
jsonSituacoes = '{%22listar_situacoes_venda%22:{%22chave%22:%22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'
jsonBuscarCPFCNPJ = '{%22buscar_cnpj%22: {%22cnpj%22:%2206787718000156%22,%22chave%22: %22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'
jsonDepartamentos = '{%22listar_departamentos%22:{%22chave%22: %22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'
jsonListVendedores = '{%22listar_vendedores%22:{%22cod_usuario%22:%22209%22,%22chave%22:%22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'
jsonGrupoProdutos = '{%22listar_grupos_prod%22:{%22chave%22:%22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}'

exemplos:





http://201.86.129.99:9009/gwservicos/execForcaVendas.rule?sys=GFS&json={%22listar_vendedores%22:{%22cod_usuario%22:%22209%22,%22chave%22:%22B5850213-D758-F2D5-3A4B-3BFAFC1BC284%22}}
