import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = 'logs'
log_filepath = os.path.join(log_dir,'running_logs.log')
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,

    handlers = [
        logging.FileHandler(log_filepath), # loglar anlık olarak aktığında logların yazılacağı dosya yolu
        logging.StreamHandler(sys.stdout) # logların anlık olarak çalışabilmesi sistemden alınmasını sağlıyor
    ]
)

logger = logging.getLogger('Text_Summarizer_Logger') # başka dosyalardan bu loglamayı import etmek için logger ismiyle çağırmak için kullandık