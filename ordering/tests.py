from django.test import TestCase
from django.core.exceptions import ValidationError
from ordering.models import Comment

class CommentModelTest(TestCase):

    def setUp(self):
        self.comment = Comment.objects.create(
            comment_id="comment1",
            content="This is a test comment.",
            rating=4
        )

    def test_comment_creation(self):
        self.assertIsInstance(self.comment, Comment)
        self.assertEqual(self.comment.comment_id, "comment1")
        self.assertEqual(self.comment.content, "This is a test comment.")
        self.assertEqual(self.comment.rating, 4)

    def test_str_method(self):
        self.assertEqual(str(self.comment), "comment1")

    def test_invalid_rating(self):
        with self.assertRaises(ValidationError):
            comment = Comment(
                comment_id="comment2",
                content="This is another test comment.",
                rating=6  # Invalid rating, should be between 1 and 5
            )
            comment.full_clean()  # This will trigger the validation

    def test_blank_rating(self):
        comment = Comment.objects.create(
            comment_id="comment3",
            content="This is a test comment with no rating."
        )
        self.assertIsInstance(comment, Comment)
        self.assertIsNone(comment.rating)

    def test_parent_comment(self):
        parent_comment = Comment.objects.create(
            comment_id="parent_comment",
            content="This is a parent comment.",
            rating=5
        )
        child_comment = Comment.objects.create(
            comment_id="child_comment",
            content="This is a child comment.",
            rating=4,
            parent_comment=parent_comment
        )
        self.assertEqual(child_comment.parent_comment, parent_comment)
        self.assertIn(child_comment, parent_comment.replies.all())