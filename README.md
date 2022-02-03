# caj2pdf_batch

糊的一个自用脚本，代码极其简单。。

结合 [caj2pdf](https://github.com/caj2pdf/caj2pdf) 使用

## 安装方法

1. clone [caj2pdf](https://github.com/caj2pdf/caj2pdf) 到本地，并安装必要依赖
2. clone 本项目到本地
3. 把 `caj2pdf_batch.py` 复制到 caj2pdf 项目文件夹下

## 使用方法

1. 终端进入caj2pdf 项目文件夹
2. 创建 `caj_to_convert` 与 `output_pdfs`文件夹
3. 把待转换的 caj 文件放入 `caj_to_convert` 文件夹
4. 在 caj2pdf 项目目录执行 `python caj2pdf_batch.py`
5. 转换后的文件在 `output_pdfs`

## 依赖

 [caj2pdf](https://github.com/caj2pdf/caj2pdf) 依赖于 [mutool](https://mupdf.com/) 与 [pyPDF2](https://github.com/mstamy2/PyPDF2)，需要另外安装

pyPDF2 通过 `pip install pypdf2`安装

mutool 官网只提供了打包好的 Windows 程序，很多人不知道 mutool 的包名。通过命令行安装即可:

Macos:

`brew update && brew install mupdf mupdf-tools`

Linux:

`apt update && apt-get install mupdf mupdf-tools `

## 注意

windows用户请移步 [caj2pdf-qt](https://github.com/sainnhe/caj2pdf-qt)，已经有带图形界面的项目了，Release里有编译好的

因此本脚本适用于有 python 环境且懒得自己编译 caj2pdf-qt 的非 Windows 用户

有极少部分特定格式的 caj 文件无法转换成功，caj2pdf 项目对此有解释。这类文件只能通过知网阅读器打印另存为的方式导出pdf。
