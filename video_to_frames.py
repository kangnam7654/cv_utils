import argparse
import os
from pathlib import Path
import cv2


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_file", type=str)
    parser.add_argument("--output_dir", type=str)
    parser.add_argument("--prefix", type=str, default=None)
    parser.add_argument("--ext", type=str)
    parser.add_argument("--interval", type=int, default=1)
    parser.add_argument("--seconds", type=bool, default=True)
    args = parser.parse_args()
    return args


def video_to_frames(
    video_file, output_dir, prefix=None, ext="jpg", interval=1, seconds=True
):
    """
    Extract frames from video.

    Args:
        video_file (str): 비디오 파일 경로
        output_dir (str): 이미지 파일이 저장될 디렉토리 경로
        prefix (str, optional): 이미지 파일 이름에 붙일 접두사. Defaults to None.
        ext (str, optional): 이미지 파일 확장자. Defaults to 'jpg'.
        interval (int, optional): 캡처 간 간격(초 또는 프레임). Defaults to 1.
        seconds (bool, optional): interval을 초 단위로 사용할지 여부. Defaults to True.
    """

    out_dir = output_dir
    os.makedirs(out_dir, exist_ok=True)

    video = cv2.VideoCapture(video_file)  # Read video file

    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))  # Count net frames
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Define unit of interval.
    if seconds:
        interval_ = round(fps * interval)
    else:
        interval_ = interval

    # | Print |
    print(f"Total frames : {total_frames}")
    print(f"FPS : {fps}")
    print(f"interval : {interval_}")

    frame_count = 0
    naming_count = 0

    while True:
        ret_val, frame = video.read()  # read_frame

        if ret_val:
            # | Save frame |
            if frame_count % interval_ == 0:
                if prefix is None:
                    output_file = os.path.join(out_dir, f"{naming_count:06d}.{ext}")
                else:
                    output_file = os.path.join(
                        out_dir, f"{prefix}_{naming_count:06d}.{ext}"
                    )
                cv2.imwrite(output_file, frame)  # 이미지 파일로 저장
                print(f"Saved: {output_file}")
                naming_count += 1
        else:  # fail
            print("Video processing complete.")
            break
        frame_count += 1
    video.release()


def main(args):
    video_to_frames(
        video_file=args.video_file,
        output_dir=args.output_dir,
        prefix=args.prefix,
        ext=args.ext,
        interval=args.interval,
        seconds=args.interval,
    )


if __name__ == "__main__":
    args = get_parser()
    main(args)
