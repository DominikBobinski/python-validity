"""Defines various constants for firmware files"""

from .usb import SupportedDevices

FIRMWARE_URIS = {
    SupportedDevices.DEV_90: {
        'driver': 'https://download.lenovo.com/pccbbs/mobiles/n1cgn08w.exe',
        'referral': 'https://support.lenovo.com/us/en/downloads/DS120491',
        'sha512': 'd839fa65adf4c952ecb4a5c4b2fc5b5bdedd8e02a421564bdc7fae1d281be4ea26fcde2333f2ab78d56cef0fdccce0a3cf429300b89544cdc9cfee6d0fe0db55'
    },
    SupportedDevices.DEV_97: {
        'driver': 'https://download.lenovo.com/pccbbs/mobiles/nz3gf07w.exe',
        'referral': 'https://download.lenovo.com/pccbbs/mobiles/nz3gf07w.exe',
        'sha512': 'a4a4e6058b1ea8ab721953d2cfd775a1e7bc589863d160e5ebbb90344858f147d695103677a8df0b2de0c95345df108bda97196245b067f45630038fb7c807cd'
    },
    SupportedDevices.DEV_9a: {
        'driver': 'https://download.lenovo.com/pccbbs/mobiles/nz3gf07w.exe',
        'referral': 'https://download.lenovo.com/pccbbs/mobiles/nz3gf07w.exe',
        'sha512': 'a4a4e6058b1ea8ab721953d2cfd775a1e7bc589863d160e5ebbb90344858f147d695103677a8df0b2de0c95345df108bda97196245b067f45630038fb7c807cd'
    },
    SupportedDevices.DEV_9d: {
        'driver': 'https://download.lenovo.com/pccbbs/mobiles/nz3gf07w.exe',
        'referral': 'https://download.lenovo.com/pccbbs/mobiles/nz3gf07w.exe',
        'sha512': 'a4a4e6058b1ea8ab721953d2cfd775a1e7bc589863d160e5ebbb90344858f147d695103677a8df0b2de0c95345df108bda97196245b067f45630038fb7c807cd'
    },
    SupportedDevices.DEV_92: { # FIXME innoextract does not like these archives:
        'driver': 'https://ftp.hp.com/pub/softpaq/sp88501-89000/sp88710.exe',
        'referral': 'https://ftp.hp.com/pub/softpaq/sp88501-89000/sp88710.exe',
        'sha512': '40354cfdda7c3fe1cf5812e676ba69e5b100e3dfe6cb9cb2532256913f9b4de2e2b2630531f61f59fc10bd448b32069fd43853c93ca0fb5df2ed0112495437dc'
    }
}

FIRMWARE_NAMES = {
    SupportedDevices.DEV_90: '6_07f_Lenovo.xpfwext',
    SupportedDevices.DEV_97: '6_07f_lenovo_mis_qm.xpfwext',
    SupportedDevices.DEV_9a: '6_07f_lenovo_mis_qm.xpfwext',
    SupportedDevices.DEV_9d: '6_07f_lenovo_mis_qm.xpfwext',
    SupportedDevices.DEV_92: '6_07f_hp_8x8pb.xpfwext'
}
