#!/usr/bin/python3
from pytube import YouTube, Playlist, Channel
from sys import argv, exit
from datetime import datetime
import colorama as col
import logging
from threading import Thread as thr
from . import __version__,__author__

if "--usage" in argv:
    argv.extend(["url", "a"])
import os, argparse

(
    cwd,
    totals,
) = os.getcwd(), {"count": 0}
logging.basicConfig(
    format="%(asctime)s -%(levelname)s -%(message)s - (%(lineno)s)",
    datefmt="%d-%b-%Y %H:%M:%S",
    level=logging.INFO,
)
output = lambda a, b: a + str(b) + col.Fore.RESET
exit_t = lambda: exit(output(col.Fore.RED, ">>Goodbye!"))


class main:
    def __init__(self, url8):
        self.url = url8[0]
        self.no = url8[1]
        if args.static:
            self.out = lambda x: print(
                output(col.Fore.YELLOW, f"[*] Downloading [{self.no}]:")
                + output(col.Fore.CYAN, x),
                end="\r",
            )
        else:
            self.out = lambda x: print(
                output(col.Fore.YELLOW, f"[*] Downloading [{self.no}]:")
                + output(col.Fore.CYAN, x)
            )
        self.out_not = lambda e1: print(
            output(col.Fore.WHITE, self.url + " : Not downloaded! -")
            + output(col.Fore.RED, e1)
        )
        if args.directory:
            self.dir = args.directory
        else:
            if args.mp3:
                self.dir = "Downloads/Audio"
            else:
                self.dir = "Downloads/Video"

    # Creates the download object
    def yt(self):
        try:
            yt = YouTube(
                url=self.url,
                on_progress_callback=self.on_progress,
                on_complete_callback=self.on_complete,
            )
        except Exception as e:
            logging.error(str(e))
            rp = None
        else:
            rp = yt
        finally:
            return rp

    # Formats int to ensure consistency of values being displayed
    def fmt(self, val):
        val = str(val)
        if len(val) != 5:
            dot = val.index(".")
            if dot == 1:
                val = "0" + val
            else:
                val = val + "0"
        if len(val) != 5:
            return self.fmt(val)
        return val

    # Shows download progress per video in %
    def on_progress(self, stream, chunk, bytes_remaining):
        if args.thread:
            return None
        progress = (
            f"{self.fmt(round(100 - (bytes_remaining/stream.filesize * 100),2))}%"
        )
        print(
            output(
                col.Fore.GREEN,
                f">>{self.fmt(round(stream.filesize/1000000,2))} MB Complete By: {progress}",
            )
            + "  Rem: "
            + output(col.Fore.YELLOW, self.fmt(round(bytes_remaining / 1000000, 2)))
            + " MB",
            end="\r",
        )

    # Executes upon download completion
    def on_complete(self, stream, file_path):
        if args.show:
            print("File_path:", file_path)
        if args.mp3:
            t = file_path.replace(cwd + "/", "")
            fp = t.replace("mp4", "mp3")
            try:
                os.system(f"mv '{file_path}' '{fp}'")
            except:
                pass

    # Updats threads count
    def update_count(self):
        if totals["count"] % args.thread == 0:
            rp = True
        else:
            rp = False
        totals["count"] = totals["count"] + 1
        return rp

    # Downloads audio
    def audio(self):
        try:

            def _download():
                yt = self.yt()
                nm = yt.title + ".mp3"
                self.out(nm)
                yt.streams.get_audio_only().download(self.dir)

            if args.thread:
                t1 = thr(
                    target=_download,
                )
                t1.start()
                if self.update_count():
                    t1.join()
            else:
                _download()
        except Exception as e:
            with open("download_failed.txt", "a", encoding="utf-8") as file:
                file.write(self.url)
            self.out_not(e)

    # Downloads video
    def video(self):
        rs = ["720p", "1080p", "4k", "480p", "360p", "240p", "144p"]
        disp = lambda nm, r: self.out(nm + ".mp4" + f" ({output(col.Fore.GREEN,r)})")

        res = args.resolution.lower()
        try:

            def _download():
                yt = self.yt()
                disp(yt.title, res)
                yt.streams.get_by_resolution(res).download(self.dir)

            if args.thread:
                t1 = thr(
                    target=_download,
                )
                t1.start()
                if self.update_count():
                    t1.join()
            else:
                _download()
        except Exception as e:
            e = str(e).lower()
            if "keyboard" in e or "eof" in e:
                exit_t()
            rs.remove(res)
            for reso in rs:
                try:

                    def _download():
                        yt = self.yt()
                        disp(yt.title, reso)
                        yt.streams.get_by_resolution(reso).download(self.dir)

                    if args.thread:
                        t1 = thr(target=_download)
                        t1.start()
                        if self.update_count():
                            t1.join()
                    else:
                        _download()
                except Exception as e:
                    e = str(e).lower()
                    if "keyboard" in e or "eof" in e:
                        exit_t()
                        break
                    if reso == rs[5]:
                        self.audio()
                        break
                else:
                    break


# Hunts down video links
class handler:
    def __init__(self):
        self.time = self.time()
        self.targets = ["fnm", "url", "playlist"]

    # Opens filepath containing links
    def opener(self, fnm):
        try:
            with open(cwd + "/" + fnm) as file:
                ct = []
                for line in file.read().split("\n"):
                    if bool(line):
                        ct.append(line)
                return (True, ct)
        except Exception as e:
            return (False, e)

    # Get links from playlist
    def playlist(self, link):
        sorted = []
        try:
            for vid in Playlist(link).videos:
                sorted.append(vid.watch_url)
        except Exception as e:
            exit(logging.critical(str(e)))
        return sorted

    # Get links from channel
    def channel(self, link):
        sorted = []
        try:
            for vid in Channel(link).videos:
                sorted.append(vid.watch_url)
        except Exception as e:
            exit(logging.critical(str(e)))
        return sorted

    # Main method
    def main(self):
        links, rp = [], True
        t, dt = args.category, args.url
        if t == "playlist":
            links.extend(self.playlist(dt))
        if t == "channel":
            links.extend(self.channel(dt))
        elif t == "url":
            links.extend(dt.split(","))
        elif t == "fnm":
            r, data = self.opener(dt)
            if r:
                links.extend(data)
            else:
                rp = False
                links.append(data)
        return (rp, links)

    # Handles current time
    class time:
        def __init__(self):
            self.__st = lambda a: str(a)

        # C_time
        def now(self):
            now = datetime.today()
            return self.__st(now.strftime("%H:%M:%S"))

        # C_date
        def date(self, pret=True):
            now = datetime.today()
            if pret:
                rp = self.__st(now.strftime("%d-%b-%Y"))
            else:
                rp = self.__st(now.date())
            return rp

        # C_datetime
        def today(self, rev=False):
            if rev:
                rp = self.now() + " " + self.date()
            else:
                rp = self.date() + "  " + self.now()
            return rp


# Formats the usage info
def usage():
    from tabulate import tabulate

    args1 = ["url", "playlist", "channel", "fnm"]
    args2 = ["--res", "--mp3", "--show", "--max", "--dir", "--static"]
    args11 = [
        "Url (link) of YouTube video",
        "Url (link) of YouTube playlist",
        "Url (link) of YouTube channel",
        "Path file containing Youtube video-links",
    ]
    args22 = [
        "Video resolution [144p,240p,360p,480p,720p,1080p,4k]",
        "Download audio only",
        "Show download path",
        "Maximum downloads [playlist/channel]",
        "Specifies directory for saving files.",
        "Restricts printing of downloaded files in prose format",
    ]
    data1 = []
    data2 = []
    for x in range(6):
        if x < 4:
            data1.append([args1[x], args11[x]])
        data2.append([args2[x], args22[x]])
    tbl = lambda data: tabulate(
        data, headers=["Command", "Function"], tablefmt="orgtbl"
    )
    print(
        output(
            col.Fore.RED,
            "\n\nRequired arguments.\n",
        )
    )
    print(output(col.Fore.CYAN, tbl(data1)))
    print(
        output(
            col.Fore.YELLOW,
            "\n\nPositional arguments.\n",
        )
    )
    print(output(col.Fore.GREEN, tbl(data2)))


def launch():
    global args
    parser = argparse.ArgumentParser(prog="yt5")
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s v{__version__}"
    )
    parser.add_argument(
        "category",
        nargs="?",
        default="url",
        choices=["fnm", "url", "playlist", "channel"],
        metavar="[fnm|url|playlist|channel]",
        help="Category of the videos referred by the link or filename[fnm] containing links",
    )
    parser.add_argument(
        "-res",
        "--resolution",
        choices=["720p", "1080p", "4k", "480p", "360p", "240p", "144p"],
        metavar="[720p|480p|360p|240p|144p]",
        help="Resolution [quality] of videos to be downloaded in",
        default="720p",
    )
    parser.add_argument(
        "-max",
        "--maximum",
        help="Maximum videos to be downloaded",
        default=100000,
        type=int,
    )
    parser.add_argument(
        "-thr",
        "--thread",
        help="Thread download process with the specified amount",
        type=int,
    )
    parser.add_argument(
        "-dir", "--directory", help="Directory for saving downloaded file"
    )
    parser.add_argument(
        "--mp3", action="store_true", help="Specify to download audio only"
    )
    parser.add_argument(
        "--show", action="store_true", help="Show the downloaded file-path"
    )
    parser.add_argument(
        "--static",
        action="store_true",
        help="Restricts stdout of file-path in prose-format",
    )
    parser.add_argument(
        "--usage", action="store_true", help="Show this help info in more stylistic way"
    )
    parser.add_argument("url", help="Link of the video")
    args = parser.parse_args()
    if args.usage:
        usage()
        exit()
    yt = handler()
    url = yt.main()
    audio = ["mp3", "audio"]
    max = lambda v: print(output(col.Fore.RED, f"Maximum downloads reached! [{v}]"))
    if url[0]:
        amt = args.maximum
        x, y = 0, len(url[1])
        print(
            output(col.Fore.RED, f"[•] Total links [{output(col.Fore.CYAN,str(y))}] :")
            + output(col.Fore.CYAN, yt.time.today())
        )
        if args.mp3:
            for data in url[1]:
                if not bool(data):
                    continue
                try:
                    x += 1
                    main((data, x)).audio()
                except KeyboardInterrupt:
                    exit_t()
                    break
                if x == amt:
                    max(amt)
                    break
        else:
            for data in url[1]:
                if not bool(data):
                    continue
                try:
                    x += 1
                    main((data, x)).video()
                except KeyboardInterrupt:
                    exit_t()
                    break
                if x == amt:
                    max(amt)
                    break
    else:
        print(output(col.Fore.RED, "There's an Error!"))
        print(url[1])
        usage()
    print(output(col.Fore.BLUE, f"\n[*]~Done : {yt.time.now()}"))

if __name__ == "__main__":
    launch()
