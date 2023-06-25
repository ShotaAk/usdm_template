# USDM (Universal Specification Describing Manner) Template

[![Deploy](https://github.com/ShotaAk/usdm_template/actions/workflows/deploy.yaml/badge.svg)](https://github.com/ShotaAk/usdm_template/actions/workflows/deploy.yaml)

USDMを適用した要求仕様書をAsciiDocで記述するためのテンプレートです。

## テンプレートの使用例

- [USDM Templateの要求仕様書](https://shotaak.github.io/usdm_template/)

## テンプレートの特徴

- AsciiDocでUSDMを適用した要求仕様書を記述できる
- 初めてAsciiDocを触る人でも記述できるシンプルな構成
- 要求と仕様の末尾には、GitHub Issue投稿用のリンクが生成される

## 使い方

asciidoctorのインストール

```sh
$ sudo apt install asciidoctor
```

テンプレートのダウンロード

```sh
$ git clone https://github.com/ShotaAk/usdm_template.git
```

AsciiDocファイルをコンパイルからHTMLファイルを生成

```sh
$ cd usdm_template
$ asciidoctor requirements_specification.adoc
```

生成されたHTMLファイルをブラウザで開く

```sh
$ google-chrome requirements_specification.html
```

### 要求仕様書の書き方

要求仕様書を追加する場合は、`chapters`ディレクトリに`adoc`ファイルを追加します。

追加したファイルを`requirements_specification.adoc`にincludeします。

```adoc
include::chapters/something.adoc[]
```

`adoc`ファイルに要求を追加する場合は、`snippets/requirements.adoc`を使用します。

- `:id:`には、要求のIDを指定します。
- `:requirement:`には、要求を指定します。
- `:reason:`には、要求の理由を指定します。
- `:explanation:`には、要求の説明を指定します。

```adoc
:id: INPUT001
:requirement: シンプルなディレクトリ構成にしたい
:reason: ディレクトリ構成が複雑だと、テンプレートを使いこなせないため
:explanation: ディレクトリとは、リポジトリのルートにあるディレクトリを指す
include::snippets/requirement.adoc[]
```

`adoc`ファイルに仕様を追加する場合は、`snippets/specification.adoc`を使用します。

- `:id:`には、仕様のIDを指定します。
- `:specification:`には、仕様を指定します。

```adoc
:id: INPUT002-01
:specification: テンプレートの最上位層に置くadocファイルはrequirements_specification.adocのみとする
include::snippets/specification.adoc[]
```

## テンプレートの仕様

[USDM Templateの要求仕様書](https://shotaak.github.io/usdm_template/)
を参照してください。

## LICENSE

Apache License Version 2.0
