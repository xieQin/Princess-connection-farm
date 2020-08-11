# INI文件配置解读

|              项              |                             说明                             |  属性  | 备注 |       例        |
| :--------------------------: | :----------------------------------------------------------: | :----: | :--: | :-------------: |
|            debug             |                           输出日志                           |  bool  |      |      False      |
|  trace_exception_for_debug   | 开启后，所有的try向上传递错误信息，并且只用第一个device跑第一个任务（单进程） |  bool  |      |      False      |
|      use_template_cache      |                 在开发工具使用时可以将其关闭                 |  bool  |      |      True       |
|        baidu_ocr_img         |      是否输出名为 baidu_ocr.bmp的图片，该图片为原生截图      |  bool  |      |      False      |
|           s_sckey            |                     s_sckey为Server酱API                     | string |      | SCU6390~94d830b |
|           log_lev            | log_levServer酱的日志等级，微信日志等级 仅有0/1/2/3，越小越详细，注意每天接口调用有上限！ |  int   |      |        1        |
|          log_cache           |                       日志缓冲消息条数                       |  int   |      |        3        |
|         baidu_apiKey         |                  baidu_apiKey为百度ocr api                   | string |      | SCU6390~94d830b |
|       baidu_secretKey        |                 baidu_secretKey为百度ocr api                 | string |      | SCU6390~94d830b |
| anticlockwise_rotation_times |      根据baidu_ocr.bmp需要逆时针旋转90°多少次截图才正向      |  int   |      |        1        |
|    async_screenshot_freq     |                     异步截图一次休眠时间                     |  int   |      |        5        |
|     bad_connecting_time      |                      异步判断异常的时间                      |  int   |      |       30        |
|        fast_screencut        |                       mincap 快速截图                        |  bool  |      |      True       |
|     fast_screencut_delay     | 由于截图太快造成脚本崩溃，可以使用这个加上全局的截图delay，模拟卡顿。 | float  |      |       0.5       |
|    fast_screencut_timeout    |                      等待服传输数据超时                      | float  |      |       10        |
|         end_shutdown         |                   非常“危险”的Windows功能                    |  bool  |      |      True       |
|       lockimg_timeout        |               90秒如果还在lockimg，则跳出重启                |  int   |      |       90        |

------

小脚印

- 2020/8/5 By:CyiceK