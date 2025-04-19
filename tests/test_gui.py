# Thank god for chatGPT that is all i have to say - Justin

import pytest
from unittest.mock import MagicMock, patch
from road_to_waffle_house.gui import start_gui, open_prompt_window, on_submit, play_audio, open_final_window, run


# Simplified test for start_gui
@patch('gui.ImageTk.PhotoImage')
@patch('PIL.Image.open')
@patch('threading.Thread')
@patch('pygame.mixer.init')
@patch('pygame.mixer.Sound')
def test_start_gui_with_button(mock_sound, mock_mixer, mock_thread,
                                mock_image_open, mock_PhotoImage):
    mock_image = MagicMock()
    mock_image.size = (600, 400)
    mock_image.mode = "RGB"
    mock_image.resize.return_value = mock_image
    mock_image_open.return_value = mock_image

    mock_main_window = MagicMock()
    mock_main_window.tk = MagicMock()

    with patch('gui.tk.Tk', return_value=mock_main_window):
        mock_photo_image = MagicMock()
        mock_photo_image.__str__.return_value = "pyimage1"
        mock_photo_image.tk = mock_main_window.tk
        mock_PhotoImage.return_value = mock_photo_image

        start_gui(run_loop=True)

        mock_image_open.assert_called_once()
        mock_PhotoImage.assert_called_once()


# Test for open_prompt_window
def test_open_prompt_window():
    with patch('tkinter.Tk') as MockTk, \
         patch('tkinter.Label') as MockLabel, \
         patch('tkinter.Entry') as MockEntry, \
         patch('tkinter.Frame') as MockFrame:

        mock_main_window = MagicMock()
        MockTk.return_value = mock_main_window

        mock_prompt_label = MagicMock()
        MockLabel.return_value = mock_prompt_label
        mock_entry = MagicMock()
        MockEntry.return_value = mock_entry

        mock_frame = MagicMock()
        MockFrame.return_value = mock_frame

        open_prompt_window()

        mock_prompt_label.pack.assert_any_call(pady=40)
        mock_prompt_label.pack.assert_any_call(pady=5)


# Test for valid input in on_submit
def test_on_submit_valid_input_valid_distance_matrix_done():
    with patch('tkinter.Entry') as MockEntry, \
         patch('tkinter.Label') as MockLabel, \
         patch('gui.open_final_window') as MockOpenFinalWindow, \
         patch('gui.run') as MockRun, \
         patch('gui.distance_matrix') as MockDistanceMatrix:

        mock_entry = MagicMock()
        MockEntry.return_value = mock_entry
        mock_entry.get.return_value = "valid_input"

        mock_error_label = MagicMock()
        MockLabel.return_value = mock_error_label

        MockRun.return_value = "info"
        MockDistanceMatrix.done = True

        on_submit()

        MockOpenFinalWindow.assert_called_once_with("info")


# Test for empty input in on_submit
def test_on_submit_with_empty_input_shows_error():
    with patch('gui.entry') as mock_entry, \
         patch('gui.error_label') as mock_error_label:
        
        mock_entry.get.return_value = ""

        on_submit()

        mock_error_label.config.assert_called_once_with(text="Invalid input")


# Test for play_audio
def test_play_audio(monkeypatch):
    mock_sound1 = MagicMock()
    mock_sound2 = MagicMock()

    monkeypatch.setattr("gui.pygame.mixer.init", MagicMock())

    def mock_sound(file):
        return mock_sound1 if "ambiance" in file else mock_sound2

    monkeypatch.setattr("gui.pygame.mixer.Sound", mock_sound)
    monkeypatch.setattr("gui.time.sleep", MagicMock(side_effect=Exception("stop loop")))

    with pytest.raises(Exception) as excinfo:
        play_audio()

    assert "stop loop" in str(excinfo.value)

    mock_sound1.set_volume.assert_called_once_with(1.0)
    mock_sound2.set_volume.assert_called_once_with(0.2)


# Test for invalid input in on_submit
def test_on_submit_invalid_input():
    with patch("gui.entry") as mock_entry, \
         patch("gui.error_label") as mock_error_label, \
         patch("gui.run") as mock_run, \
         patch("gui.distance_matrix") as mock_distance_matrix:

        mock_entry.get.return_value = "invalid address"
        
        mock_run.return_value = "info"
        mock_distance_matrix.done = False

        on_submit()

        mock_error_label.config.assert_called_once_with(text="Invalid input")


# Test for open_final_window
@patch('gui.ImageTk.PhotoImage')
@patch('PIL.Image.open')
@patch('tkinter.Tk')
@patch('tkinter.Label')
@patch('tkinter.Frame') 
def test_open_final_window(mock_frame_class, mock_label, mock_tk, mock_image_open, mock_photo_image):
    mock_image = MagicMock()
    mock_image.size = (300, 200)
    mock_image.resize.return_value = mock_image
    mock_image_open.return_value = mock_image

    mock_main_window = MagicMock()
    mock_main_window._w = "."
    mock_tk.return_value = mock_main_window

    mock_frame = MagicMock()
    mock_frame_class.return_value = mock_frame

    info = ["You are 10 miles away", "Distance from Waffle House"]

    open_final_window(info)

    mock_tk.assert_called_once()
    mock_image_open.assert_any_call("photos/you_are.png")
    mock_image_open.assert_any_call("photos/from.png")
    mock_image_open.assert_any_call("photos/logo.png")

    mock_photo_image.assert_any_call(mock_image)

    call_args = mock_label.call_args_list[0]
    label_parent = call_args[0][0]
    assert label_parent == mock_frame, f"Expected {mock_frame}, but got {label_parent}"

    label_image = call_args[1]["image"]
    assert label_image == mock_photo_image.return_value, f"Expected {mock_photo_image.return_value}, but got {label_image}"
    assert call_args[1]["bg"] == "black", "Expected bg='black'"

    mock_label.return_value.pack.assert_any_call(pady=10)
    mock_main_window.mainloop.assert_called_once()
