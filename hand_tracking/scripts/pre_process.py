def landmarks(image, landmarks):
    def calc_landmark_list(image, landmarks):
        image_width, image_height = image.shape[1], image.shape[0]
        landmark_point = []
        for _, landmark in enumerate(landmarks.landmark):
            landmark_x = min(int(landmark.x * image_width), image_width - 1)
            landmark_y = min(int(landmark.y * image_height), image_height - 1)
            # landmark_z = landmark.z

            landmark_point.append([landmark_x, landmark_y])

        return landmark_point

    landmark_list = calc_landmark_list(image, landmarks)

    import copy
    import itertools


    def pre_process_landmark(landmark_list):
        temp_landmark_list = copy.deepcopy(landmark_list)

        # 相対座標に変換
        base_x, base_y = 0, 0
        for index, landmark_point in enumerate(temp_landmark_list):
            if index == 0:
                base_x, base_y = landmark_point[0], landmark_point[1]

            temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
            temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y

        # 1次元リストに変換
        temp_landmark_list = list(
            itertools.chain.from_iterable(temp_landmark_list))

        # 正規化
        max_value = max(list(map(abs, temp_landmark_list)))

        def normalize_(n):
            return n / max_value

        temp_landmark_list = list(map(normalize_, temp_landmark_list))

        return temp_landmark_list

    pre_processed_landmark_list = pre_process_landmark(landmark_list)
    return pre_processed_landmark_list
