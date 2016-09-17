import re


class Cleaner:
    """The Cleaner-Class tries to get the raw extracted text of the extractors
    in a comparable format. For this it deletes unnecessary whitespaces
    or in case of readability html-tags which are still in the extracted
    text.
    """

    def delete_tags(self, arg):
        """Removes html-tags from extracted data.

        :param arg: A string, the string which shell be cleaned
        :return: A string, the cleaned string
        """
        return re.sub(r'<([\w\s\d:="/\\!?äüö.-]*)>', '', str(arg))

    def delete_whitespaces(self, arg):
        """Removes newlines, tabs and whitespaces at the beginning, the end and if there is more than one.

        :param arg: A string, the string which shell be cleaned
        :return: A string, the cleaned string
        """
        # Deletes whitespaces after a newline
        arg = re.sub(r'(?<=\n)( )+', '', str(arg))
        # Deletes every whitespace, tabulator, newline at the beginning of the string
        arg = re.sub(r'^[ \t\n\r\f]*', '', arg)
        # Deletes whitespace or tabulator if followed by whitespace or tabulator
        arg = re.sub(r'[ \t]+(?=([ \t]))', '', arg)
        #  Deletes newline if it is followed by an other one
        arg = re.sub(r'[ \n]+(?=(\n))', '', arg)
        # Deletes newlines and whitespaces at the end of the string
        arg = re.sub(r'[ \n]*$', '', arg)
        return arg

    def do_cleaning(self, arg):
        """Does the actual cleaning by using the delete methods above.

        :param arg: A string, the string which shell be cleaned
        :return: A string, the cleaned string
        """
        if arg is not None:
            arg = self.delete_tags(arg)
            arg = self.delete_whitespaces(arg)
            return arg
        else:
            return None

    def clean(self, list_article_candidates):
        """Iterates over each article_candidate and cleans every extracted data.

        :param list_article_candidates: A list, the list of ArticleCandidate-Objects which have been extracted
        :return: A list, the list with the cleaned ArticleCandidate-Objects
        """
        # Save cleaned article_candidates in results.
        results = []

        for article_candidate in list_article_candidates:

            article_candidate.title = self.do_cleaning(article_candidate.title)
            article_candidate.description = self.do_cleaning(article_candidate.description)
            article_candidate.text = self.do_cleaning(article_candidate.text)
            article_candidate.topimage = self.do_cleaning(article_candidate.topimage)
            article_candidate.author = self.do_cleaning(article_candidate.author)
            article_candidate.publish_date = self.do_cleaning(article_candidate.publish_date)

            results.append(article_candidate)

        return results
