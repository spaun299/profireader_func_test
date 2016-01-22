from rodynni_firmy import start_test as start_rodynnifirmy_test
import argparse
parser = argparse.ArgumentParser(description='Test for profireader or rodynnifirmy')
parser.add_argument("site")
parser.add_argument("device")
args = parser.parse_args()

if __name__ == '__main__':
    if 'rodynnifirmy' in args.site:
        start_rodynnifirmy_test(device=args.device.split("'")[-2])
