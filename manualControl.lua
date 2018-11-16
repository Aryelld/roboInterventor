--codigo para forma manual
h={-1,-1,-1}
robo = simGetObjectHandle('Omnirob')
h[1]=simGetObjectHandle('Omnirob_FLwheel_motor')
h[2]=simGetObjectHandle('Omnirob_FRwheel_motor')
h[3]=simGetObjectHandle('Omnirob_RRwheel_motor')
h[4]=simGetObjectHandle('Omnirob_RLwheel_motor')
v={-1,-1,-1} 
v1=10
while true do
    message,data,data2=simGetSimulatorMessage()
    v[1] = simGetJointTargetVelocity(h[1])
    v[2] = simGetJointTargetVelocity(h[2])
    v[3] = simGetJointTargetVelocity(h[3])
    v[4] = simGetJointTargetVelocity(h[4])
    fatorDesacelera = 0.01
    fatorRotacao = 0.5
    if message==sim_message_keypress then
        if (data[1]==2010) then -- rightkey
            simSetJointTargetVelocity(h[1],fatorRotacao*v1+fatorDesacelera*v[1])
            simSetJointTargetVelocity(h[2],fatorRotacao*v1+fatorDesacelera*v[2])
            simSetJointTargetVelocity(h[3],fatorRotacao*v1+fatorDesacelera*v[3])
            simSetJointTargetVelocity(h[4],fatorRotacao*v1+fatorDesacelera*v[4])
        else 
            if (data[1]==2009) then -- left key
                simSetJointTargetVelocity(h[1],-fatorRotacao*v1+fatorDesacelera*v[1])
                simSetJointTargetVelocity(h[2],-fatorRotacao*v1+fatorDesacelera*v[2])
                simSetJointTargetVelocity(h[3],-fatorRotacao*v1+fatorDesacelera*v[3])
                simSetJointTargetVelocity(h[4],-fatorRotacao*v1+fatorDesacelera*v[4])
            else 
                if(data[1]==2007) then -- up key
                    simSetJointTargetVelocity(h[1],v1+v[1])
                    simSetJointTargetVelocity(h[2],-v1+v[2])
                    simSetJointTargetVelocity(h[3],-v1+v[3])
                    simSetJointTargetVelocity(h[4],v1+v[4])
                    --simAddStatusbarMessage("^")
                else 
                    if (data[1]==2008) then -- down key
                        simSetJointTargetVelocity(h[1],-v1+v[1])
                        simSetJointTargetVelocity(h[2],v1+v[2])
                        simSetJointTargetVelocity(h[3],v1+v[3])
                        simSetJointTargetVelocity(h[4],-v1+v[4])
                        --simAddStatusbarMessage("v")
                    else
                        if (data[1] == 32) then --space key
                        simSetJointTargetVelocity(h[1],0)       
                        simSetJointTargetVelocity(h[2],0)
                        simSetJointTargetVelocity(h[3],0)
                        simSetJointTargetVelocity(h[4],0)
                        --simAddStatusbarMessage("stop")
                        end
                    end
                end
            end
        end 
    else
        if (not v[1] == 0) then
            simSetJointTargetVelocity(h[1],fatorDesacelera*v[1])
        end   
        if (not v[2] == 0) then
            simSetJointTargetVelocity(h[2],fatorDesacelera*v[2])
        end   
        if (not v[3] == 0) then
            simSetJointTargetVelocity(h[3],fatorDesacelera*v[3])
        end   
        if (not v[4] == 0) then
            simSetJointTargetVelocity(h[4],fatorDesacelera*v[4])
        end   
    end
end