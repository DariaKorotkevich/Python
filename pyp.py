def main(x):
    match x[3], x[0]:
        case 2004, 2009:
            match x[4], x[2]:
                case "OPAL", 1981: return 0
                case "OPAL", 1996: return 1
            match x[4], x[1]:
                case "PERL6", "CUDA": return 2
                case "PERL6", "VOLT": return 3
        case 2004, 1965: return 4
        case 2004, 2008:
            match x[4]:
                case "OPAL": return 5
            match x[4], x[1]:
                case "PERL6", "CUDA": return 6
                case "PERL6", "VOLT": return 7
    match x[3], x[4]:
        case 2007, "OPAL": return 8
        case 2007, "PERL6":
            match x[1], x[2]:
                case "CUDA", 1981: return 9
                case "CUDA", 1996: return 10
            match x[1]:
                case "VOLT": return 11


print(main([2009, 'VOLT', 1981, 2007, 'OPAL']))
print(main([1965, 'CUDA', 1981, 2004, 'PERL6']))
print(main([1965, 'CUDA', 1981, 2007, 'PERL6']))
print(main([2009, 'VOLT', 1996, 2004, 'PERL6']))
print(main([2008, 'CUDA', 1996, 2007, 'PERL6']))

print(main([2009, 'VOLT', 1981, 2007, 'PERL6']))
