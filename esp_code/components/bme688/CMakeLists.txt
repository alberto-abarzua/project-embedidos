idf_component_register(SRCS "bme68x.c" "bme_main.c"
                       INCLUDE_DIRS "include"
                       REQUIRES driver esp_timer i2cdev esp_idf_lib_helpers )

