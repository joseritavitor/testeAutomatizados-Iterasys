from behave import given, when, then
from utils import Utils
from pages.validador import Validador
from pages.precovenda import PrecoVenda
from pages.precoassinante import PrecoAssinante
from pages.header_page import HeaderPage
from pages.nomeproduto import NomeProduto
from nose.tools import assert_equal
from time import sleep

utils = Utils()
header_page = HeaderPage()
validador = Validador()
precovenda = PrecoVenda()
nomeproduto = NomeProduto()
precoassinante = PrecoAssinante()

@given(u'que da acesso ao site Petz')
def step_impl(context):
    utils.navegar('https://www.petz.com.br')


@given(u'preencho o input de pesquisa')
def step_impl(context):
    header_page.preenche_imput_busca('Ração ')
    sleep(3)
    header_page.preenche_imput_busca('Golden Fórmula Senior para Cães Adultos Sabor Frango e Arroz - 15kg')
    sleep(3)

@when(u'clico no botão de pesquisar')
def step_impl(context):
    header_page.button_click_get()

@then(u'traz o retorno de minha pesquisa')
def step_impl(context):
    assert_equal(nomeproduto.get_product_name(),'Ração Golden Fórmula Senior para Cães Adultos Sabor Frango e Arroz - 15kg')


@when(u'validação do fornecedor')
def step_impl(context):
    assert_equal(validador.get_text_provider(), 'Premier Pet')

@then(u'validação do preço do produto')
def step_impl(context):
    assert_equal(precovenda.get_value_sale(), 'R$ 150,90')


@then(u'validação do preço para assinante')
def step_impl(context):
    assert_equal(precoassinante.get_value_sale(), 'R$ 135,81')

