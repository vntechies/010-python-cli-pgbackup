from argparse import Action, ArgumentParser
import time


class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = ArgumentParser(
        description="""
        CLI tool back up Postgre database về local hoặc S3 sử dụng Python
        """
    )

    parser.add_argument("url", help="Connection string của Postgres DB")
    parser.add_argument(
        "--driver",
        "-d",
        help="Chọn phương thức và vị trí lưu file backup",
        nargs=2,
        metavar=("DRIVER", "DESTINATION"),
        action=DriverAction,
        required=True,
    )
    return parser


def main():
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    timestamp = time.strftime("%Y-%m-%dT%H-%M", time.localtime())
    file_name = pgdump.dump_file_name(args.url, timestamp)
    if args.driver == "s3":
        client = boto3.client("s3")
        print(f"Upload file backup lên S3 với tên file {file_name}")
        storage.s3(client, dump.stdout, args.destination, file_name)
    else:
        outfile = open(args.destination, "wb")
        print(f"Lưu file backup tại local với tên file {outfile.name}")
        storage.local(dump.stdout, outfile)
