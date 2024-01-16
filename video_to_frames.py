import os
from pathlib import Path
import cv2


def video_to_frames(
    video_file, output_dir, prefix=None, ext="png", interval=1, seconds=True
):
    """
    비디오 파일을 이미지로 분해합니다.

    Args:
        video_file (str): 비디오 파일 경로
        output_dir (str): 이미지 파일이 저장될 디렉토리 경로
        prefix (str, optional): 이미지 파일 이름에 붙일 접두사. Defaults to None.
        ext (str, optional): 이미지 파일 확장자. Defaults to 'png'.
        interval (int, optional): 캡처 간 간격(초 또는 프레임). Defaults to 1.
        seconds (bool, optional): interval을 초 단위로 사용할지 여부. Defaults to True.
    """

    success = True
    frame_count = 0
    naming_count = 0
    last_stem = ""

    if isinstance(video_file, list):
        pass  # Do Nothing
    else:
        video_file = list(video_file)

    for idx, f in enumerate(video_file):
        success = True  # success 리셋
        frame_count = 0  # 비디오마다 프레임 리셋

        if isinstance(output_dir, list):
            out_dir = output_dir[idx]
        else:
            out_dir = output_dir
        os.makedirs(out_dir, exist_ok=True)  # 출력 디렉터리가 없으면 생성

        video = cv2.VideoCapture(f)  # 비디오 파일 읽기

        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # 비디오 파일의 총 프레임 수를 확인
        fps = int(video.get(cv2.CAP_PROP_FPS))  # FPS 확인
        print(f"Total frames: {total_frames}")

        # interval의 단위를 결정합니다.
        if seconds is True:
            interval_ = round(fps * interval)
        else:
            pass  # do nothing

        while success:
            success, frame = video.read()  # 프레임을 읽음

            if success:
                if frame_count % interval_ == 0:
                    # ========= File Naming =======
                    if prefix is None:
                        output_file = os.path.join(out_dir, f"{naming_count:06d}.{ext}")
                    else:
                        output_file = os.path.join(
                            out_dir, f"{prefix}_{naming_count:06d}.{ext}"
                        )
                    cv2.imwrite(output_file, frame)  # 이미지 파일로 저장
                    print(f"Saved: {output_file}")

                    current_stem = os.path.split(out_dir)[-1]
                    if current_stem != last_stem:
                        naming_count = 0
                    else:
                        naming_count += 1
                    last_stem = current_stem
            else:  # fail
                print("Video processing complete.")
            frame_count += 1
        video.release()


def recurrent_run():
    from glob import glob

    directory = Path("/home/kangnam/hdd/datasets/metaworld/customization")
    video_root = directory.joinpath("videos")
    image_root = directory.joinpath("images")
    video_files_in = glob("**/*.mp4", root_dir=os.fspath(video_root), recursive=True)

    image_path = [os.fspath(image_root.joinpath(x).parent) for x in video_files_in]
    video_files = [os.fspath(video_root.joinpath(x)) for x in video_files_in]
    video_to_frames(video_file=video_files, output_dir=image_path, interval=0.3)


if __name__ == "__main__":
    recurrent_run()
    # video_file, output_dir = temp_paths()
    # video_to_frames(video_file, output_dir)
