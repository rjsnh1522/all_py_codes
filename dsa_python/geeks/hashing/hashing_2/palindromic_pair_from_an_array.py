class Solution:
    def __init__(self):
        self.result = []

    def check_palindrome(self, string):
        if len(string) == 0:
            return True
        if string == "":
            return True
        start = 0
        end = -1
        if string[start] == string[end]:
            string = string[1:-1]
            self.check_palindrome(string)
            return True
        else:
            return False

    def solve(self, A):
        self.result = []
        arr = A
        hash_table = {arr[i][::-1]: i for i in range(len(arr))}

        for i in range(len(arr)):
            for j in range(len(arr[i])):
                prefix_str = arr[i][: (j + 1)]
                if prefix_str in hash_table and i != hash_table[prefix_str]:
                    remaining_str = arr[i][(j + 1):]
                    if self.check_palindrome(remaining_str):
                        self.result.append([i, hash_table[prefix_str]])
                suffix_str = arr[i][-(j + 1):]
                if prefix_str == suffix_str:
                    continue
                if suffix_str in hash_table and i != hash_table[suffix_str]:
                    remaining_str = arr[i][: -(j + 1)]
                    if self.check_palindrome(remaining_str):
                        self.result.append([hash_table[suffix_str], i])
        return self.result


A = [
    "hrcucojwqunjbajhraornrsjwmbxacvtcnijljvchbyatpikyvskhvawrjggovlojquglfkcfxkgzughpr",
    "hjhmsvu",
    "kkneaoftyihexaqrprdtviyqn",
    "sdsndmbrhtznciludmdovjzhdebngmsgjpeanpmvmvgvqukgadksugbwlxdytwinhzwawlpdfxvzbckntcwyofsfedaxyvb",
    "qbybpfrwpsx",
    "xgrlazltjzggattmfovxgszewltzewzwihiiivrrgpezejvgwshgkmitabataltr",
    "jlfhnnhocstikrxzsscqrvfraqpvawjvmewtjtgbevyyoegkxkecptbwchjobvysgewuxfwsjxguxkbmbik",
    "mrjrulijvmutcbdhorvozukucdnevdsdawiwnaomkzxtjtcexvfavgbqwxuvlmaswoltdkwjcgdossrqadvftorszasddr",
    "swllfjianpqmcoakqpieqaipmuqtinxngqyn",
    "rzhgsetdseetqpkgvaxkxvmckljcownrpzpyoebcxnrlpaqlimvqnpip",
    "qzsissrhbyremwslxexryrgnhbfuprsghydkqpholssrmrufwihuoueixbxsihicuflybbwguvsvavwrt",
    "kylnfriegoxtiljekaqujlzqszjxauvqkbobpfafqqqyrabmomttoicyavmjiceetvsergkd",
    "wrbzkesncvbxgeczsucobgaexbgghebb",
    "iqabvbkdmtbwplzrdxnkuadyvaxosfankpnqjvrehbmdnwrkgtoklnxudjlksexotzwrsaiqpjagsfuhhiutbxnjobdugrgavpef",
    "mzwevqgokzqlxmosjodlil",
    "xmao",
    "brgdtsdgyklkscrsjclkzruijfqgjykttgnbmfmxwoeikqtndwmmlqpwjqxyjotqytmhbrckocxpowldumnkaedfq",
    "axujscyqghawgidlvdwglgpfngqd",
    "tgwpfwrectdyhlypdmargudvznuktdvhusvtsydcpgucbmkkiirelqukwzmlvhzsdcaevfitnwdhshlcxclnrdorougexit",
    "abflptfnvfezxcibwsqvbjjozeabamgtw",
    "lczupowwwndhppauhmghhfjtkpdcrzqh",
    "gxbzklmjtesdktjjblofqwnlncyqawtlacloggrwkkvvsuhvs",
    "rtvjtvunkmgjjxkqdlvbzzudwplnthmiybbheurhqftoyjzzdeyymkjoxex",
    "uvnsafiekpxbsmnolcwbbramjqpglwmqgecenezhkygehbbsjhrwufsooyyjejqbrvdmrxydkgbqmikrehfhlyzgwpd",
    "i",
    "lajbrphzpnxjiqsngfeyxhdndwefzthvuxqczvzubqk",
    "orqzreycuelzjbjxbcsdiiebfhgyuarliheqbqkebhvgeothsizigdjbvqm",
    "avgpqdrjgecfibcyufjsiskzdeyzvpdwuzqy",
    "abcd",
    "qpljuebnokxhoywzrzlogqkbgyldjsixjsueqrtjrwjyvjlaryzpaohntffrfvkhsuwjchstohun",
    "tapurszyfyzylzpasaeabfhenlwfjxlagczeaaufcmlxoqutkfpmpujzveivrnrkyfvtgdcklzxpksotvkobticindutene",
    "xepdyebjufmypbhdowoq",
    "emrdrdzlsjfodhegdudskbyfxzgiibhwqnxospgw",
    "dcba",
    "uwwlxvfwtddqpxysazmukvjgqbrkqddeabdukqdxsdjnppttfobicobxutdzflxxsejb",
    "iplhdcmdvoypxqazweecjecwfrqcrp",
    "hpqcmqdksbpsdvt",
    "efclsiqkwlufsvqkhdpfdsdzmldwdcwvzkgrbohkfyejgakybniuvn",
    "ilykocdhrcxyjmbgqdnaiptwzmzmscbavtdnwtsxxbpnljlaw",
    "ilceecjqedtckeveclkxrchocoxuchlmeqydegyhcwrmmnzrxvaniemlxhddsfuljbhrnakeisdzlxkrkffqcq",
    "rtdcswmdrvmhdxuxnyblrhn",
    "cmwtsedqeeidfzilqarvdoicbshlgefiuprdwfxvvxxkqbawzaqztbdpkmleqdzgbdwcjspqqpvti",
    "uffkmjmdrgpreyzkwgmrbwrvcgczdmhzczgieglyuhrfzicrejlweakukczifzertgsdosipqwciuliwhagupddmyfkwdhsaihqq",
    "fgyfsuvkkttbocklovavvonwffkfzcjlpzkybhwoofxvrgjmukmnxbge",
    "pmlunxxwozwlcecdnqnjrucaljmdhpwoiauoncromlozzkjyam",
    "kfkvtmpaecpyrprzshokdakzqctelm",
    "ayzyvoptwrtwuxgmbmzmajqcxhytvwtwkxnrufoewxwtjfwcqlcaozdtmdfrykclxofzvtbtkahpuekuckkkaadahtnu",
    "gkdejkcwojwexpheriufxtvvdqapiaxcgumbydejyovxclwnd",
    "cxgqiwvtbqpowxxgfyw",
    "raoveozdezouthtddzcichfjxdaffatfqngpnwexptxfjtfjgrkythlzxnqhopst",
    "ombtbzoywchtivpielwoqovwvhfklx",
    "jwcbipbjixudxynzdivb",
    "vlpbfofrrobvyncdclnzxvmpuddtfigqgumyn",
    "gekjwzvxoouymengeyeiqkypsccdxgsnaikgizsuydurepgaaugvuggqqeddvungtzwbsqgduojqvykfwwzqqyhjblnx",
    "h",
    "zjajrtvimsmk",
    "encjeujjudqkksommpwcuecjumkylwuivqabcyhimvkuwuyvwapctmzlxohfsinemktsuvofdauxdqvwogsusknlhdyui",
    "ctrlscoryjxbcnfgdcnncjpdjpchtqemqrcafommelyhahigbyufkfqgfqfqchibqfbwxqyvdswmdjyheykw",
    "uvji",
    "rshezbxhmunuvxjlqiadzznujeqkghstsasgnkbsufhrkjnpdjidcmvnomnixslbyelxkhbfmwpdsvtqnrfrnxdlxdcdtekvag",
    "oanbgjurhjfrvwvncvoeoqoqzi",
    "qvziwpsiatkwzcczazpyozszvzhtiozmohqpkocmjwrgsdcvxhpncwucnuyhoilnehgrjznbgdgmsactobbgljdsjzssodjdlcbs",
    "mcsr",
    "dlpnzjqcuocckgfrmtpkjksuyulkgwcyzuzizorfcgksouqbes",
    "gitmhytlnfqoxjojnnqmiaefb",
    "gzhnxwgficmgmnfprdoyqwfhphxxmgmfnhzwpuzmlppoytqchpczjuckgbkseko",
    "vjkojwwnthinghmnsilrgazoycbwnnrqspfqgebzlnaunshghjjivwfnqwgqgrz",
    "xqhjhxmedaxtehpwcrgwmtupxlywpgoscfzukdjjwcjpgijpbihgefypllydrbcnsygmnnobfrwezjhype",
    "wfwseoegonhewmggaknlueaosxckyahueisiukgiidlliuemjrcgdcw",
    "aybwpo",
    "lbmfmpnoitpynvkmuuottbe",
    "kmbaginvvfkizwkegspnuuyqqiaenhdmtfkccrcexmdaddwlmqowbllntpvdbuxh",
    "cnhdyrufjfkdivjrdqcgqdqmsohlnyquoqtddlvxozzbvualhwobspeahtykwbomfbxwszlxet",
    "zdtbobllqvlujjpcrkfwkqzs",
    "lbxomubonvcjmwfowfkuzh",
    "sfygxprrqvrgpihjqjhtuonqqknmdfqvynnnzfyuo",
    "paozvfbnnxmdrhruwpztfheofkpuldjfbukfgzcnshzsyasexyxbfihoahxsforteqestchruvmzoc",
    "jdxxoowpktbgruktnpjfnsprzddruodkmstkotdsiyacbgduswtlje",
    "icsyirlxjtdtkplmnvjkiuzazoqqpglwobvfzkipyrtshhrikqblkogcnxankumt",
    "mpbzcpxurcpyirzxohapoqiicehiahzwcmirorfoqmrpwvoehgeldurqqlrstlaoeubkuzyriskcspvxuqbhcyjgteihfrgqv",
    "fleeflnxwjhzxyrhtzxa",
    "ydmzdypiinqqniocnzrfdisjkamcziacyshuxvxtuidjpkoierievbvpdpgojtarnv",
    "ktxwgadhmusflekjiaqbmtjhmdmyrbxrepvpmwlsuhgdimniihmnwpnignkswvimfqwdpkghwhapmvpilxwodb",
    "vyegqgzdfzgwpahsicueuvxfwxdkdatwdlzwaqscmyttqhkmjait",
    "cpjdxiyzuiqgvcpwcy",
    "powybcdllwpzgaqeujkwvpvifahwswcqnbrynivkzncczdgbrrzxvdbla",
    "opfoxhqmidwdulddnhvuozrnxnuckmjhojzerccuhwijcxklwccxbaqesnmddti",
    "brerukwgbroojuavbbfesvjdfqbqjjsvphaldemgjdbshjynkomtxdhovcgrcelrzspbvssph",
    "jjkjpaukhmsotsgxflddltzrqodjyotpwvizkoklptcfwuschtpexvhtoaldlgpdhjdhdkgaelzixxsdiwxapj",
    "oedujidjeuzppxrjbproxhdqcbsxvotwdiib",
    "ouubwbognrcrcwyguoxjtusuapga",
    "rexfangljmtlbrmuiloyovtiqu",
    "qtbatxneckyhptbqugildnrpalatwilaqpgmhycxexbraebqfvnr",
    "codoshjxbldbjxngesipdnjgramzigjlgwrulregvxgwgvplvvcvhcuccaxzusbpbeduez",
    "fbgyroeqodjvwbgpvkpscetgnemra",
    "vdtsprrbakoikiabhdlbverprzkjxrclnplziqidodkefzpqm",
    "tonpfxhkairocxumqokeu",
    "wqksxhkdwrtzssbcxjvqr",
    "pcnoxp",
    "pjomhud",
]

# arrs = ["abc", "sa", "xy", "as", "abcd", "dcba", "lls", "s", "ssll"]
# arrs = ["abc", "sa", "xy", "as"]
res = Solution()
print(res.solve(A))
