import socket
import ctypes
import binascii
import time


# Use the ip and the port set is the games udp settings
UDP_IP = "127.0.0.1"
UDP_PORT = 5003


print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

# Motion data
MotionData = binascii.unhexlify('e207010069b6f822031dff94149a393f1e0000000196990ec4c3094ec05f69d343342d06bc54708e3fec0eccbadb80fbff45f1bb0e0000db80a496dd39a2b1aabbb245b6bc5ed3d7bfbc1335b9a2b24e37172711c4144e44c04b79b7431bd71440a5c57dba1855afc1840db5ffb980477f0000840d78de653c831784baf71a85ba6d4a4240ad4b8c392f1ec6373d1a04c4aeeaf03f8822a0c330226d418dffbc3db9611ec1e466b400dfb3224cbfffe466a80098bf3366673e176893bd204d0d40ea0f54bb67ec023be0b31cc4798e61c04f7f2a44fc1696409104f03ecd8ea1c27707d3003a80c67fba00780720702bbe03b34b3e3b463cbd85534540e16cc6bbac6ababbe07f1ac4fa1039c027540b44093cf1401706d13ee0e4a3c2c10bb9008d80737f2101c30bcff587bd0e547c3e295129bcbe2c4340f67718bc9d9410bc06c1b8c302b48dc0edb14744af6b03c16dfefbbef0b6ab42d1f35aff697f9680e9ffd1f32c01af3cb7c53dbd3ceb403d0345c3bdaf799cba24d53a3ac78c47c3ed25ac40c85867c42ae6a9427e16383f303e50c1957e220116edf212f4fa7c7e1574a8bf9bd30a3e7e03fdbc3314dc3f327240bb6a98213dfbf143c2483c90bfb7e48ac3b20186c2dbe4c73f738867422b9f5c02aa5352acffff269fa96f1dbe9e1cbf3d1f61a33de2ae5bbf6961643cff4a1c38322d09c45fdb9a3fe91a4bc39df8a040ccb3d33e02b787c2720969005b80a57f53ff7209e7c0c93c916724c0c7f1483d5c55444015e9a43b4624ad3b7aba19c46e6434c0cc560944ae05ef40ccd4cf3e9d56aac2090bb3007c80837f1e010b0b28f84dbb535b1d3ec3d22ebc0a8943408fb016bcae770fbc4ed7a7c331be17c0ed24d64314f0fbc02283e6bee8fda64200f46aff6e7f92801f0000f4a2e2133dc395863eae095f3d4053c0bd348c0d3ad18b7fbabbd31e43d601d440e9396cc453ac2242fe52cfbd6d48f0bfdc7f23ff2efad505ee01d97fa3357e3efc7a0cc01c7269bdc5e5ce3ff019c73b630877bc3f6efec3094d2d400d9ed6c3224e24c1d7c6813e45f62ac201e296009383697cecfdffe154a501bfc738023f12c3543c30eb39c0d0368a3c3a19853ca689fdc336c8064039eca3c38df38e419077113e9ab3e8c06078710082d47f2b81fe5e78c0bc9c3fcfa843bf32e57ebda371f53f71583d3af8e43f3cd5c2a9c3e35228c04f04ed437695fac0a7b101bf1fb1a74216f44dff707f90803c0017f4cf773b3dc248623eaa58d13c24ecbebdda17ad3a4fe5f0ba35a7cb43c35ca240204f83c4d1d676423472c2be4b95abc1e47847fff5d5062a9cfde078c718023d64742b3fc79e963d4fe2f33f407c3c3c9c40993c27f19fc3651aa2bf5f9883438713e4c0e5d511bfb23e98420cf425ff6f7f9480050210f48190d4bcbe78d13eedf5c2bc8d8ebfbdba2f773c664a81bcd15ef642f5a3d24025d56bc4d4617e424ec0013e33e22cc0e37faaffc3fa3e05c800e27fad56b83e71485bc003cb593b874ece3fbde41c3ba1f3c8bbab860fc476cf4bc063d0e4433d9c72bae0968b3f18c54bbcdb80ecff46f1ba0efcffdb803d57d23dd2e31abc3702d5bc28d3d7bf52861bba38840339cf97cdc2e0f8c040931f69c4de89af42e5a9ec3ed66785c0d87fcb00e2f92106a9fdd37f324e47bb6680dd3d942ea4bd3132cf3faaf7aebbdcfc953c59792e3f828b2b3fa7f8a33faa6ba33f0aad18c0ed993a40755b00c0c2aa1840d7b910c3591d4c43ea5bc9c217162843a786b0413487b041d858b041de59b0415dea813afad2803ae9a3afb719e9aeb73cc7ef3a60b54c3def50b0410c0deab929b794392d13c3bb43aceb3be8a6fd39ae77c0bd9c1be338')
# Session Data
SessionData = binascii.unhexlify('e207010169b6f822031dff946da2893f2d00000001001f1835a6160a0b00630c201c500000ff0011265fd03c00486aa53d00f6e8053e0026e53e3e02d7346e3e0070418c3e008b2cae3e00d607cf3e024e9ef63e0001c8073f008c5f163f00e3601e3f009e26283f001c5d433f00dac05c3f00577b6a3f007dac713f0000000000000000000000000000000000000000000000')

# LapData = binascii.unhexlify('e207010269b6f822031dff94797e873f2c00000001b765ad4259917445b765ad42f051a040f051a0400078374387b52f4800000080131f00010000110006c06bb3421a8a774100000000000000000000000000887543920a7f4800000080042e010000000f030220e3ab421a144241e073aa42000000000000000000de6a440eb87f4800000080032e00000000050402e0c3ab42c115ab426018ab4200fadc4180a2ea41408bb34500c07e4800000080052d0002000004040260acae42ef5d623fa0c9ac42000000000000000000909142d835794800000080112d0000000013040260fbaf42613d95425f60af42009bdf418055f041a01b9a45fa4a784800000080122c000200000a04026014ae429001d841008bad420000000000000000801bdd44dddd7a48000000800c2d000000000704020037af42be87624200a1ad42001bdb418017e841004e6a45decc7c4800000080092d00020000090402a0f5af421a1f1741a505ae42000000000000000000874f442df37948000000800f2d000000001204022079b042759a713f80c2ad42000000000000000000f8a3422538794800000080102d000000000b040200e8ad42c10c8a4207daad4200c3d94100bbec4120778e455f977d4800000080072d00020000010402a08aad4290cdf241d026ad4200acdc410000000040fa03458f337b48000000800b2d000100000804020006ae4290478841d87fad42000000000000000000dc87445e337a48000000800d2d000000000d04022094ae421a3054418256ad42000000000000000000067144ac147a48000000800e2d000000000e0402a0baad4261b48b425b92ac42005cdc41001ced4100e78f45dea27d4800000080062d0002000002040240aaaa424a69124240aaaa420021dc410000000040551645fb7c7b48000000800a2d000100000c040240d5ae4241c88742cbbeae4200dfdd4100afef41203589454f6d7d4800000080082d00020000060402003dab429058ea4140d7aa42803cda4100000000002a0245ec6a804800000080012e00010000000402cca5ae42d4867445cca5ae42f051a040f051a04000801443a306194800000080141b000100001000060083ab421025d4412001ab4200000000000000000050e944e84f804800000080022e00000000030402')

counter = 0
# dataGroup = [MotionData, SessionData, LapData]
dataGroupName = ['MotionData', 'SessionData']
dataGroup = [MotionData, SessionData]

sending_sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sending_sock.sendto(dataGroup[counter], (UDP_IP, UDP_PORT))



while True:
    # Rotate through the list of data packets
    counter+= 1
    if counter == 2:
        counter = 0

        
    # Sleeps for 2 seconds to slow down and actually be able to read the output it is sending
    time.sleep(2)
    print 'Sending', dataGroupName[counter]
    sending_sock.sendto(dataGroup[counter], (UDP_IP, UDP_PORT))

    
