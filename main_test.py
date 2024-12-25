import unittest
from main import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager("test_tasks.json")

    def tearDown(self):
        import os
        if os.path.exists("test_tasks.json"):
            os.remove("test_tasks.json")

    def test_add_task(self):
        self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0]["title"], "Test task")
        self.assertFalse(self.manager.tasks[0]["completed"])

    def test_add_task_invalid(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")

    def test_list_tasks(self):
        self.manager.add_task("Task 1")
        self.manager.add_task("Task 2")
        self.assertEqual(len(self.manager.tasks), 2)

    def test_mark_completed(self):
        self.manager.add_task("Test task")
        self.manager.mark_completed(1)
        self.assertTrue(self.manager.tasks[0]["completed"])

    def test_delete_task(self):
        self.manager.add_task("Task to delete")
        self.manager.delete_task(1)
        self.assertEqual(len(self.manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
