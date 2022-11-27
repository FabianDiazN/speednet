
import speedtest

velocidad = speedtest.Speedtest()
print("""
                    .:/++oo++/:.                   
              .+ymMMMMMMMMMMMMMMmy+.              
           -smMMMMNhso+////+oshNMMMMms-           
         /dMMMNy/`    .---..    `/yNMMMd/         
        .NMMh:   :ohmMMMMMMMMmho:   :hMMN.        
         `:.  -yNMMMNhyooooyhNMMMNy-  .:`         
             oMMMh+.   `..`   .+hMMMo             
             `+o.  :sdMMMMMMds:  -o+`             
                 .mMMMdyssydMMMm.                 
                 `oyo`      `oyo`                 
                       +hh/                       
                      `NMMN                       
                       `::`
+----------------------------------------------------------------------+
| ________                     _________        _____   __      _____  |
| __  ___/________ _____ _____ ______  /        ___  | / /_____ __  /_ |
| _____ \ ___  __ \_  _ \_  _ \_  __  / __________   |/ / _  _ \_  __/ |
| ____/ / __  /_/ //  __//  __// /_/ /  _/_____/_  /|  /  /  __// /_   |
| /____/  _  .___/ \___/ \___/ \__,_/           /_/ |_/   \___/ \__/   |
|        /_/                                                           |
+______________________________________________________________________+
"""
)

print("▓ ▓ ▓ ▓ ▓ ▓ ▓ Midiendo velocidad ▓ ▓ ▓ ▓ ▓ ▓ ▓")
print("Tu velocidad de Descarga es:", velocidad.download()/1000000)
print("Tu velocidad de Subida es: ", velocidad.upload()/1000000)
print("Ping: ", velocidad.results.ping)


