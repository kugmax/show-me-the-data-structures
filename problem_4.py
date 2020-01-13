class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def is_contain_user(self, user):
        return user in self.users


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    def loop(group):
        if group.is_contain_user(user):
            return True

        for g in group.groups:
            is_in_group = loop(g)
            if is_in_group:
                return True

        return False

    return loop(group)


def assert_equals(expected, actual):
    assert (expected == actual), "expected {0}, actual {1}".format(expected, actual)


def assert_true(actual):
    assert_equals(True, actual)


def when_group_is_empty():
    parent = Group("parent")

    assert_true(not is_user_in_group("user_1", parent))
    assert_true(not is_user_in_group("user_2", parent))
    assert_true(not is_user_in_group("user_3", parent))


def when_there_is_one_group():
    parent = Group("parent")
    parent.add_user("user_1")
    parent.add_user("user_2")

    assert_true(is_user_in_group("user_1", parent))
    assert_true(is_user_in_group("user_2", parent))

    assert_true(not is_user_in_group("user_3", parent))


def when_there_are_many_sub_groups():
    group_1 = Group("group_1")
    group_1.add_user("user_1_A")
    group_1.add_user("user_1_B")

    group_1_1 = Group("group_1_1")
    group_1_1.add_user("user_1_1_A")

    group_1_2 = Group("group_1_2")
    group_1_2.add_user("user_1_2_A")
    group_1_2.add_user("user_1_2_B")

    group_1_1_3 = Group("group_1_1_3")
    group_1_1_3.add_user("user_1_1_3_A")
    group_1_1_3.add_user("user_1_1_3_B")

    group_1_1.add_group(group_1_1_3)
    group_1.add_group(group_1_1)
    group_1.add_group(group_1_2)

    assert_true(is_user_in_group("user_1_A", group_1))
    assert_true(is_user_in_group("user_1_1_A", group_1))
    assert_true(is_user_in_group("user_1_2_B", group_1))
    assert_true(is_user_in_group("user_1_1_3_B", group_1))
    assert_true(not is_user_in_group("user_1_1_3_C", group_1))
    assert_true(not is_user_in_group("user_1_1_3_C", group_1_1_3))
    assert_true(is_user_in_group("user_1_2_B", group_1_2))


if __name__ == "__main__":
    when_group_is_empty()
    when_there_is_one_group()
    when_there_are_many_sub_groups()

