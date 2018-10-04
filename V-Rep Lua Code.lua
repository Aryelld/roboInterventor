h={-1,-1,-1}
robo = simGetObjectHandle('Omnirob')
h[1]=simGetObjectHandle('Omnirob_FLwheel_motor')
h[2]=simGetObjectHandle('Omnirob_FRwheel_motor')
h[3]=simGetObjectHandle('Omnirob_RRwheel_motor')
h[4]=simGetObjectHandle('Omnirob_RLwheel_motor')
v1=50
while true do
    message,data,data2=simGetSimulatorMessage()
    if message==sim_message_keypress then
        if (data[1]==2010) then -- rightkey
            local rot=0
            local previousAngle=simGetObjectOrientation(robo,-1)[3]
            while true do
                message,data,data2=simGetSimulatorMessage()
                angle = simGetObjectOrientation(robo,-1)[3]
                local da=angle-previousAngle
                if da>=0 then
                    da=math.mod(da+math.pi,2*math.pi)-math.pi
                else
                    da=math.mod(da-math.pi,2*math.pi)+math.pi
                end
                rot=rot+da
                previousAngle=angle
                if message==sim_message_keypress or math.abs(rot)>=math.pi/2 then                    
                    simSetJointTargetVelocity(h[1],0)       
                    simSetJointTargetVelocity(h[2],0)
                    simSetJointTargetVelocity(h[3],0)
                    simSetJointTargetVelocity(h[4],0)
                    break
                else
                    fator = (math.pi/2 - math.abs(rot))^2.25
                    simSetJointTargetVelocity(h[1],fator*v1)
                    simSetJointTargetVelocity(h[2],fator*v1)
                    simSetJointTargetVelocity(h[3],fator*v1)
                    simSetJointTargetVelocity(h[4],fator*v1)
                end
            end            
        else 
            if (data[1]==2009) then -- left key
                local rot=0
                local previousAngle=simGetObjectOrientation(robo,-1)[3]
                while true do
                    message,data,data2=simGetSimulatorMessage()
                    angle = simGetObjectOrientation(robo,-1)[3]
                    local da=angle-previousAngle
                    if da>=0 then
                        da=math.mod(da+math.pi,2*math.pi)-math.pi
                    else
                        da=math.mod(da-math.pi,2*math.pi)+math.pi
                    end
                    rot=rot+da
                    previousAngle=angle
                    if message==sim_message_keypress or math.abs(rot)>=math.pi/2 then  
                        simSetJointTargetVelocity(h[1],0)       
                        simSetJointTargetVelocity(h[2],0)
                        simSetJointTargetVelocity(h[3],0)
                        simSetJointTargetVelocity(h[4],0)
                        break
                    else
                        fator = (math.pi/2 - math.abs(rot))^2.25
                        simSetJointTargetVelocity(h[1],-fator*v1)
                        simSetJointTargetVelocity(h[2],-fator*v1)
                        simSetJointTargetVelocity(h[3],-fator*v1)
                        simSetJointTargetVelocity(h[4],-fator*v1)
                    end
                end            
            else 
                if(data[1]==2007) then -- up key
                    simSetJointTargetVelocity(h[1],v1)
                    simSetJointTargetVelocity(h[2],-v1)
                    simSetJointTargetVelocity(h[3],-v1)
                    simSetJointTargetVelocity(h[4],v1)
                    --simAddStatusbarMessage("^")
                else 
                    if (data[1]==2008) then -- down key
                        simSetJointTargetVelocity(h[1],-v1)
                        simSetJointTargetVelocity(h[2],v1)
                        simSetJointTargetVelocity(h[3],v1)
                        simSetJointTargetVelocity(h[4],-v1)
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
    end
end