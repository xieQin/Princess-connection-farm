# encoding=utf-8
import configparser

cfg = configparser.ConfigParser()
cfg.read('config.ini', encoding="utf-8")

# cfg.sections() 全部头
# cfg.get('debug', 'trace_exception_for_debug')
# cfg.getint('log', 'log_cache')
# cfg.getboolean('debug', 'debug')
# 上面为读取的三种方法（str/int/bool)

debug = cfg.getboolean('debug', 'debug')
trace_exception_for_debug = cfg.getboolean('debug', 'trace_exception_for_debug')
use_template_cache = cfg.get('debug', 'use_template_cache')
baidu_ocr_img = cfg.getboolean('debug', 'baidu_ocr_img')

s_sckey = cfg.get('log', 's_sckey')
log_lev = cfg.get('log', 'log_lev')
log_cache = cfg.getint('log', 'log_cache')

baidu_apiKey = cfg.get('pcrfarm_setting', 'baidu_apiKey')
baidu_secretKey = cfg.get('pcrfarm_setting', 'baidu_secretKey')
anticlockwise_rotation_times = cfg.getint('pcrfarm_setting', 'anticlockwise_rotation_times')
async_screenshot_freq = cfg.getint('pcrfarm_setting', 'async_screenshot_freq')
bad_connecting_time = cfg.getint('pcrfarm_setting', 'bad_connecting_time')
fast_screencut = cfg.getboolean('pcrfarm_setting', 'fast_screencut')
fast_screencut_delay = cfg.getfloat('pcrfarm_setting', 'fast_screencut_delay')
fast_screencut_timeout = cfg.getint('pcrfarm_setting', 'fast_screencut_timeout')
end_shutdown = cfg.getboolean('pcrfarm_setting', 'end_shutdown')
lockimg_timeout = cfg.getint('pcrfarm_setting', 'lockimg_timeout')
