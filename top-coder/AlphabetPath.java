public class AlphabetPath {
    
    private boolean checkValid(String[] letterMaze, int i, int j) {
        if (i < 0 || i >= letterMaze.length || j < 0 || j >= letterMaze[i].length()) return false;
        else return true;
    }
    
    private boolean findPath(String[] letterMaze, int i, int j, int abcNumber) {
        if (!checkValid(letterMaze, i,j)) return false;
        if (abcNumber == 26) return true;
        String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        char currentLetter = alphabet.charAt(abcNumber);
        if (letterMaze[i].charAt(j) == currentLetter) {
            return findPath(letterMaze, i-1, j  , abcNumber+1) ||
                   findPath(letterMaze, i+1, j  , abcNumber+1) ||
                   findPath(letterMaze, i  , j-1, abcNumber+1) ||
                   findPath(letterMaze, i  , j+1, abcNumber+1);
        }
        return false;
    }
    
    public String doesItExist(String[] letterMaze) {
        int i = 0, j = 0;
        for (String element : letterMaze) {
            for (char letter : element.toCharArray()) {
                if (letter == 'A')
                    if (findPath(letterMaze, i, j, 0))
                        return "YES";
                j++;
            }
            j = 0;
            i++;
        }
        return "NO";
    }
    
}