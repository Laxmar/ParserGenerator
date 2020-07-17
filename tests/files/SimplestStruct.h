#ifndef STH_H_
#define STH_H_

#include ""
#include ""

namespace some_namespace {

	struct Parameters {
			float throttleValue;
			uint32_t rawThrottleValue;
			bool emergencyStop;
			bool limitedPowerMode;
			bool isBatteryInOptimalState;
	}__attribute__((packed));

}

#endif /* STH_H_ */