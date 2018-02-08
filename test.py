#!flask/bin/python
import os
import unittest
from io import BytesIO
from app import app

#location of future test images for upload
STATIC_PATH = os.path.join("./app/static/images", "test.jpg")

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #will set defaults before each test is run
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    #given an http GET to an expected path, response is a 200 and homepage info is shown
    def test_make_successful_get_to_upload_route(self):
        responseBase = self.app.get('/')
        responseUploader = self.app.get('/uploader')
        uploadTitle = "Photo Uploader"
        assert (200 == responseBase.status_code) and (200 == responseUploader.status_code)
        assert (uploadTitle in str(responseBase.data)) and (uploadTitle in str(responseUploader.data))

    #given an http GET to an extension to a non existant resource/page,
    #the request is handled but user is served an error message
    def test_invalid_paths_are_handled(self):
        responseFoo = self.app.get('/foo')
        responseBar = self.app.get('/bar')
        errorTitle = "Resource Not Found"
        assert (200 == responseFoo.status_code) and (200 == responseBar.status_code)
        assert (errorTitle in str(responseFoo.data)) and (errorTitle in str(responseBar.data))

    #given an extension to a non existant resource/page, a link is provided to the real app page
    def test_invalid_paths_link_to_valid_paths(self):
        validPath = 'href="/uploader"'
        responseFoo = self.app.get('/foo')
        htmlStr = str(responseFoo.data)
        assert validPath in htmlStr

    #given an http POST request with an image file, response should be a 200
    def test_successful_post_for_upload(self):
        data = {
            'field': 'value',
            'file': (BytesIO(b'imgimgabc123'), 'test.jpg')
        }
        response = self.app.post('/uploader', buffered=True,
                         content_type='multipart/form-data',
                         data=data,
                         follow_redirects=True)
        #remove temp image after test
        os.remove(STATIC_PATH)
        assert response.status_code == 200

    #given a successful file upload, the file's content is displayed to the user
    def test_file_content_returned_back_to_client(self):
        #the only files accepted for upload are image type files
        data = dict(
            file=(BytesIO(b'imgimgabc123'), "test.jpg"),
        )
        response = self.app.post('/uploader', buffered=True,
                         content_type='multipart/form-data',
                         data=data,
                         follow_redirects=True)
        responseStr = str(response.data)
        #remove temp image after test
        os.remove(STATIC_PATH)
        assert "imgimgabc123" in responseStr

# runs the unit tests in the module
if __name__ == '__main__':
  unittest.main()
