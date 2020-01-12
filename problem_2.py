import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    def loop(path, accumulator):
        dirs = os.listdir(path)
        for dir in dirs:
            local_path = os.path.join(path, dir)

            if os.path.isfile(local_path) and dir.endswith(suffix):
                accumulator.append(local_path)

            elif os.path.isdir(local_path):
                loop(local_path, accumulator)

        return accumulator

    result = loop(path, [])
    return result


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


def assert_equals_list(expected, actual):
    assert_equals(expected, sorted(actual))


if __name__ == "__main__":
    assert_equals_list(
        ['testdir/subdir1/a.c', 'testdir/subdir3/subsubdir1/b.c', 'testdir/subdir5/a.c', 'testdir/t1.c'],
        find_files(".c", "testdir")
    )

    assert_equals_list(
        ['testdir/subdir1/a.h', 'testdir/subdir3/subsubdir1/b.h', 'testdir/subdir5/a.h', 'testdir/t1.h'],
        find_files(".h", "testdir")
    )

    assert_equals_list(
        ['testdir/subdir2/.gitkeep', 'testdir/subdir4/.gitkeep'],
        find_files(".gitkeep", "testdir")
    )

    assert_equals_list([], find_files(".not_existed", "testdir"))

    assert_equals_list(
        ['testdir/subdir1/a.c'],
        find_files(".c", "testdir/subdir1")  # test specific sub dir
    )