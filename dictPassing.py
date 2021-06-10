if __name__=="__main__":
    def main():
        InputOutputMap = dict()
        InputOutputMap['Input'] = [(0,0), (1, 0)]
        InputOutputMap['Output'] = [(0,0)]
        connectNodes = dict()
        #connectNodes[(0,0)] = InputOutputMap

        pcu = (0,0)
        connectNodes[pcu] = {'Input':[(1,0), (0,0)],
                             'Output': [(2,0)],
                             'OutInterface': "NE"}
        print (connectNodes)

    main()
