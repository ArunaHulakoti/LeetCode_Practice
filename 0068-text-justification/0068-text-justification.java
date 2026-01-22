class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {

        List<String> result = new ArrayList<>();
        int i = 0;

        while (i < words.length) {

            int lineLen = words[i].length();
            int j = i + 1;

            // PHASE 1: Greedy packing
            while (j < words.length &&
                   lineLen + 1 + words[j].length() <= maxWidth) {
                lineLen += 1 + words[j].length();
                j++;
            }

            int wordCount = j - i;
            StringBuilder line = new StringBuilder();

            // PHASE 2: Space handling
            if (j == words.length || wordCount == 1) {
                // LEFT JUSTIFIED
                for (int k = i; k < j; k++) {
                    line.append(words[k]);
                    if (k < j - 1) line.append(" ");
                }
                while (line.length() < maxWidth) {
                    line.append(" ");
                }
            } else {
                // FULL JUSTIFIED
                int totalWordLen = 0;
                for (int k = i; k < j; k++) {
                    totalWordLen += words[k].length();
                }

                int totalSpaces = maxWidth - totalWordLen;
                int spacesEach = totalSpaces / (wordCount - 1);
                int extraSpaces = totalSpaces % (wordCount - 1);

                for (int k = i; k < j; k++) {
                    line.append(words[k]);
                    if (k < j - 1) {
                        for (int s = 0; s < spacesEach; s++)
                            line.append(" ");
                        if (extraSpaces > 0) {
                            line.append(" ");
                            extraSpaces--;
                        }
                    }
                }
            }

            result.add(line.toString());
            i = j;
        }

        return result;
    }
}
