# 宇浩·星陳

## schema

/scheme 中的文件爲 Rime 輸入法各平臺（小狼毫、鼠鬚管）碼表。

使用本方案，需要預先安裝[宇浩輸入法](https://github.com/forFudan/yuhao/releases)，以獲取相關的插件、反查、符號等文件。

請在 default.custom.yaml 文件的 patch/schema_list 列表中手動添加本方案名如下：

patch:
  schema_list:
    - schema: yustar
    - schema: yustar_tc
    - schema: yustar_tw

重新部署后即可使用。

## hotfix

/hotfix 中的文件，用於 Android 平臺的「中文輸入法」，以及一些 Rime 内核較老的程序。使用時，直接將文件覆蓋 /schema 下的原文件即可。

## mabiao

/mabiao 中的文件是其他平臺的碼表。

單字全碼表和單字簡碼表在 /mabiao/evaluation 下。
