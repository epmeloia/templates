# 🛒 Preços de Produtos e Links — Perplexity (Brasil)

- Use este template quando precisar **pesquisar preços atuais**, **comparar ofertas** e **trazer links**.  
- Modo recomendado: **🔴 Pesquisa (com web)**.

---

## 🎯 Objetivo
Encontrar **melhores opções** de compra no **Brasil**, com **preço atualizado**, **link direto**, **loja confiável** e **especificações mínimas**.

---

## ✅ Checklist rápido (antes de buscar)
- [ ] Produto, modelo e **especificações mínimas** definidos
- [ ] **Faixa de preço** e/ou teto (R$)
- [ ] **Localização BR** (preferir lojas brasileiras)
- [ ] Lojas-alvo (prioridade): **KaBuM, Amazon BR, Magazine Luiza, Americanas, Submarino, Casas Bahia, Pichau, Terabyte, Mercado Livre (oficial)**  
- [ ] Exigir **link do produto** e **data/hora da verificação**
- [ ] **Desconsiderar Marketplace estrangeiro** e anúncios duvidosos

---

## 🧩 Prompt base (cole e edite)
```

🔴 PESQUISA DE PREÇOS — BRASIL

Tarefa: pesquisar ofertas ATUAIS no Brasil para o produto abaixo.
Produto: \<nome/modelo exato>
Especificações mínimas: <listar>
Faixa de preço desejada: R\$ \<mín> a R\$ \<máx> (pode sugerir custo-benefício próximo)

Regras:

* Buscar apenas em lojas brasileiras confiáveis (ex.: KaBuM, Amazon BR, Magalu, Americanas, Casas Bahia, Pichau, Terabyte, Mercado Livre oficial).
* Ignorar lojas estrangeiras e preços sem estoque.
* Trazer link direto do produto, preço, loja, condição (novo/usado), e observações relevantes.
* Se possível, incluir opções de frete/retirada e se o preço é à vista ou no cartão.
* Informar a DATA/HORA da verificação.

Formato da resposta (tabela + lista):
Tabela com colunas: Loja | Produto/Modelo | Preço (R\$) | Condição | Link
Depois, uma lista com Observações (frete, promo relâmpago, cupons, variações de preço).

No fim, traga um resumo de Custo-Benefício (Top 3).

```

---

## 🧪 Exemplo (notebook com RTX 4070)
```

Produto: Notebook gamer RTX 4070, 16GB RAM, SSD 1TB, tela 15-16", Brasil.
Teto: R\$ 10.000
Exigir: link, preço, loja, condição.

```

---

## 🧰 Prompt de refinamento (use conforme necessário)
- **Filtrar por loja**  
```

Refine: foque apenas em KaBuM, Amazon BR, Magalu e Pichau. Refaça a tabela.

```

- **Baixar preço / custo-benefício**  
```

Traga opções até 10% acima do teto se tiverem claras vantagens (garantia, melhor GPU/CPU, tela superior).

```

- **Garantia/loja oficial**  
```

Priorize lojas oficiais e garanta que o link é de vendedor "oficial" no Mercado Livre.

```

- **Histórico/variação**  
```

Se houver, cite variações recentes de preço (sem ferramentas pagas), com links de referência.

```

---

## 🧾 Modelo de saída (copie este cabeçalho)
| Loja | Produto/Modelo | Preço (R$) | Condição | Link |
|---|---|---:|---|---|
|  |  |  |  |  |

**Observações**
- Frete/retirada:
- Pagamento (à vista/cartão):
- Promo/relâmpago/cupom:
- Observações técnicas relevantes:

**Top 3 Custo-Benefício (resumo)**
1.  
2.  
3.  

**Data/Hora da verificação:** __(preencher)__

---

## ⚠️ Cuidados importantes
- Desconfie de preços muito abaixo do mercado;
- Cheque **estoque** (evitar “indisponível”);
- Em Marketplaces, verifique **qualificação do vendedor** e **nota do produto**;
- Confirme se o preço é **à vista** (boleto/PIX) ou **no cartão** (pode variar);
- Preferir **loja oficial** quando possível.

---

## 🧭 Dicas de busca (palavras-chave)
- `<produto> <modelo> preço site:*.br`
- `<produto> <modelo> promoção`
- `<produto> <modelo> loja oficial`
- `<produto> <modelo> 16GB 1TB RTX 4070 site:kabum.com.br`

---

## 🔁 Iterar rápido
- Se não encontrar dentro do teto, peça **faixa +10%** com justificativa de benefício.
- Se surgirem muitas opções, **limite a 5 melhores** e peça **motivo do ranking**.

---

## 📌 Observação
Este template prioriza **Brasil**. Para outros países, troque as lojas e a moeda, mantendo o mesmo formato.
```
