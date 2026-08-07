#Николай Пономарев 45-я когорта, финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data

def test_create_and_get_order_by_track():
    track = sender_stand_request.post_new_order(data.ORDER_BODY)
    assert track is not None
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200