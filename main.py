from openai import OpenAI
import AO3
from pathlib import Path
import os
from gtts import gTTS, gTTSError


def get_gtts_audio(self, text_lists, save_loc):
    text = ""
    for tl in text_lists:
        text1 = " . ".join([tp for tp in tl if tp != ""])
        if text1 != "":
            text = text + " . . " + text1

    try:
        gTTS(text, lang_check=False).save(save_loc)   # (mp3_fp)
    except gTTSError as err:
        print(err.infer_msg())


class AO3Audio:
    def __init__(self):
        self.ao3_client = AO3.GuestSession()
        self.save_folder = Path.cwd() / "books"

    def set_save_folder(self, save_fol):
        self.save_folder = Path.resolve(save_fol)
    def set_ao3_user(self, username, password):
        self.ao3_client = AO3.Session(username, password)

    def get_chapter_text(self, chapter):
        # add stuff like work summary & title if it's the first chapter
        text_pieces = [
            chapter.title,
            # get chapter author if applicable
            chapter.summary,
            chapter.start_notes,
            chapter.text,
            chapter.end_notes
        ]
        return text_pieces

    def get_start_text(self, work):
        start = [
            work.title
        ]

        if len(work.authors) > 1:
            uns = [author.username for author in work.authors]

            start = start + [
                f"written by {', '.join(uns[0:-1])}, and {uns[-1]}"
            ]
        else:
            start = start + [f"written by {work.authors[0].username}"]

        start = start + [
            work.summary,
            work.start_notes
        ]
        return start
    def get_end_text(self, work):
        return [work.end_notes]

    def get_work_audio(self, work_url):
        work = AO3.Work(AO3.utils.workid_from_url(work_url), session=self.ao3_client)

        loc = self.save_folder / f"{work.title}_{work.id}.mp3"

        # ensure save_loc exists
        if not loc.parent.is_dir():
            loc.parent.mkdir(parents=True)


        # get text
        text = []
        for num, chapter in enumerate(work.chapters):
            if num == 0:
                text = text + [self.get_start_text(work), self.get_chapter_text(chapter)]
            elif num == work.nchapters-1:
                text = text + [self.get_chapter_text(chapter), self.get_end_text(work)]
            else:
                text = text + [self.get_chapter_text(chapter)]

        #use gtts
        get_gtts_audio(text, loc)



if __name__ == "__main__":
    ao3a = AO3Audio()
    #ao3a.set_ao3_user(os.environ.get("ao3_un"), os.environ.get("ao3_pw"))
    ao3a.get_work_audio("https://archiveofourown.org/works/1012337")
