# coding: utf-8

import argparse

from common import manager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--mpi4py', action="store_true",
                        dest="mpi4py", default=False,
                        help="Also switch mpi4py library")
    parser.add_argument('name', type=str,
                        help="MPI name to use")

    args = parser.parse_args()
    manager.use(args.name, mpi4py=args.mpi4py)


if __name__ == "__main__":
    main()
