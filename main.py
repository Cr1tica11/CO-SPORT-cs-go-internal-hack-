from plugins import glow
from plugins import auto_shoot
from plugins import bunny_hop 
from plugins import no_flash
def main():
    settings = {glow.Glow: True}

    for i in settings:
        if settings[i]:
            i()


if __name__ == '__main__':
    main()