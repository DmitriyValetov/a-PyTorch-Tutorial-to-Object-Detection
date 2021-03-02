from utils import create_data_lists, create_jsons_for_roboflow_pascal_voc


if __name__ == '__main__':

    # create_data_lists(voc07_path='/media/dmitriy/main/data/object_detection/pascal_voc/VOC2007',
    #                   voc12_path='/media/dmitriy/main/data/object_detection/pascal_voc/VOC2012',
    #                   output_folder='../pascal_voc_dumps')

    create_jsons_for_roboflow_pascal_voc(
        roboflow_path="../blood_voc",
        output_folder="../blood_voc_dumps"
    )