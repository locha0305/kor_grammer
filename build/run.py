import config


if __name__ == '__main__':
    try:
        config.build['main'](*config.build['factor'])
    except:
        pass
    