from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False


app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UsersTest(TestCase):
    def setUp(self):
        """Add sample user."""

        User.query.delete()

        user = User(first_name="TestUser", last_name="TestLast", image_url="https://images.unsplash.com/photo-1530813089459-29f31dd229c2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3F1YXJlc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60")
        db.session.add(user)
        db.session.commit()

        
        self.user = user

    def tearDown(self):
        """Clean up transactions."""

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('TestUser', html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/{self.user.id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(f'<h1>{self.user.first_name}', html)
            self.assertIn(self.user.last_name, html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name": "TestUser2", "last_name": "cat", "img_url": "https://images.unsplash.com/photo-1530813089459-29f31dd229c2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c3F1YXJlc3xlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"}
            resp = client.post("/users/new", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("TestUser2", html)