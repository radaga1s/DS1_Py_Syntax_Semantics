def data_types():
    res = []
    for entity in (5, '5', 0.5, True, [], {}, (), set()):
        res.append(type(entity).__name__)
    print(f"[{', '.join(res)}]")


if __name__ == '__main__':
    data_types()