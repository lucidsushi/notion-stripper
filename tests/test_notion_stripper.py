import pytest
import pytest

import notion_stripper


def test_construct_md_file_paths(mocker):
    '''
    Test that the function returns a list of file paths.
    '''
    mock_dir_return = mocker.patch('notion_stripper.os.listdir')
    mock_dir_return.return_value = ['file1.md', 'file2.md']

    file_path = notion_stripper.construct_md_file_paths('some_dir')
    assert next(file_path) == 'some_dir/file1.md'
    assert next(file_path) == 'some_dir/file2.md'
